#!/usr/bin/env python3
"""Regenerate the directory table and the monitoring table inside README.md / README.en.md.
Reads providers.json and data/probes/*.jsonl. Pure stdlib."""
import json, pathlib, datetime, statistics, re

ROOT = pathlib.Path(__file__).resolve().parent.parent
PROVIDERS = json.loads((ROOT / "providers.json").read_text(encoding="utf-8"))
NOW = datetime.datetime.now(datetime.timezone.utc)


def load_rows(days):
    since = NOW - datetime.timedelta(days=days)
    rows = []
    for f in sorted((ROOT / "data" / "probes").glob("*.jsonl")):
        for line in f.read_text(encoding="utf-8").splitlines():
            if not line.strip():
                continue
            r = json.loads(line)
            if datetime.datetime.strptime(r["ts"], "%Y-%m-%dT%H:%M:%SZ").replace(tzinfo=datetime.timezone.utc) >= since:
                rows.append(r)
    return rows


def pct(n, d):
    return "-" if d == 0 else f"{100.0 * n / d:.1f}%"


def p(vals, q):
    if not vals:
        return "-"
    vals = sorted(vals)
    k = max(0, min(len(vals) - 1, round(q * (len(vals) - 1))))
    return f"{vals[k] * 1000:.0f} ms"


def stats(rows, pid, kind, auth, base=None):
    # 只统计打到当前 providers.json 里这个 base 的样本：换过探测域名的家，旧域名的历史不混进来
    rs = [r for r in rows if r["provider"] == pid and r["kind"] == kind and r["auth"] == auth
          and (base is None or r["url"].startswith(base.rstrip("/") + "/"))]
    n = len(rs)
    up = sum(1 for r in rs if r["gateway_up"])
    ok = sum(1 for r in rs if (r["ok"] if auth else r["endpoint_ok"]))
    lat = [r["t_ttfb"] for r in rs if r["gateway_up"] and r["t_ttfb"] > 0]
    return n, up, ok, lat


def link(url, text=None):
    return f"[{text or url.replace('https://', '').rstrip('/')}]({url})" if url else "-"


def yn(url, lang):
    if url:
        return f"[{'是' if lang == 'zh' else 'yes'}]({url})"
    return "否" if lang == "zh" else "no"


def directory_table(lang):
    if lang == "zh":
        head = "| 服务商 | 官网 | Claude Code | Codex CLI | 支付方式 | 价格页 | 注册 | 备注 | 核实日期 |\n|---|---|---|---|---|---|---|---|---|\n"
    else:
        head = "| Provider | Website | Claude Code | Codex CLI | Payments | Pricing | Sign-up | Notes | Verified |\n|---|---|---|---|---|---|---|---|---|\n"
    out = head
    for pr in PROVIDERS:
        name = f"**{pr['name']}**" + ("（本仓库维护者）" if pr.get("maintainer") and lang == "zh" else " (maintainer)" if pr.get("maintainer") else "")
        pay = "、".join(pr.get("payments") or []) if lang == "zh" else ", ".join(pr.get("payments_en") or pr.get("payments") or [])
        reg = {"open": "开放" if lang == "zh" else "open", "closed": "已停止" if lang == "zh" else "closed"}.get(pr.get("registration"), "未核实" if lang == "zh" else "unverified")
        notes = pr.get("notes_en" if lang == "en" else "notes") or ""
        out += f"| {name} | {link(pr['website'])} | {yn(pr.get('claude_code_doc'), lang)} | {yn(pr.get('codex_doc'), lang)} | {pay or '-'} | {link(pr['pricing_url'], '价格' if lang == 'zh' else 'pricing') if pr.get('pricing_url') else '-'} | {reg} | {notes} | {pr.get('verified_at', '-')} |\n"
    return out


def monitor_table(lang, days):
    rows = load_rows(days)
    if lang == "zh":
        head = f"| 服务商 | 端点 | 样本数 | 网关应答率 | 端点有效率 | 应答延迟 P50 | 应答延迟 P95 | 认证请求成功率 |\n|---|---|---|---|---|---|---|---|\n"
    else:
        head = f"| Provider | Endpoint | Samples | Gateway answered | Endpoint valid | Reject latency P50 | Reject latency P95 | Authenticated success |\n|---|---|---|---|---|---|---|---|\n"
    out = head
    for pr in PROVIDERS:
        for kind, label in (("anthropic", "/v1/messages"), ("openai", "/v1/chat/completions")):
            if not pr.get("anthropic_base" if kind == "anthropic" else "openai_base"):
                continue
            base = pr["anthropic_base" if kind == "anthropic" else "openai_base"]
            n, up, ok, lat = stats(rows, pr["id"], kind, False, base)
            an, aup, aok, _ = stats(rows, pr["id"], kind, True, base)
            auth_cell = "-" if an == 0 else f"{pct(aok, an)} ({an})"
            out += f"| {pr['name']} | `{label}` | {n} | {pct(up, n)} | {pct(ok, n)} | {p(lat, 0.5)} | {p(lat, 0.95)} | {auth_cell} |\n"
    return out


def splice(text, tag, body):
    start, end = f"<!-- {tag}:START -->", f"<!-- {tag}:END -->"
    pat = re.compile(re.escape(start) + r".*?" + re.escape(end), re.S)
    if not pat.search(text):
        raise SystemExit(f"marker {tag} missing")
    return pat.sub(start + "\n" + body.rstrip() + "\n" + end, text)


def main():
    stamp = NOW.strftime("%Y-%m-%d %H:%M UTC")
    for fname, lang in (("README.md", "zh"), ("README.en.md", "en")):
        path = ROOT / fname
        text = path.read_text(encoding="utf-8")
        text = splice(text, "DIRECTORY", directory_table(lang))
        intro = (f"最近 7 天 · 更新于 {stamp} · 探测节点：GitHub Actions（美国）· 每 6 小时一轮\n\n" if lang == "zh"
                 else f"Last 7 days · updated {stamp} · vantage: GitHub Actions (US) · every 6 hours\n\n")
        text = splice(text, "MONITOR", intro + monitor_table(lang, 7))
        intro30 = ("最近 30 天\n\n" if lang == "zh" else "Last 30 days\n\n")
        text = splice(text, "MONITOR30", intro30 + monitor_table(lang, 30))
        path.write_text(text, encoding="utf-8")
        print("updated", fname)


if __name__ == "__main__":
    main()
