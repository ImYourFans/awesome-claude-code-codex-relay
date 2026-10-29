#!/usr/bin/env python3
"""Regenerate the directory table and the monitoring table inside README.md / README.en.md.
Reads providers.json and data/probes/*.jsonl. Pure stdlib."""
import json, pathlib, datetime, re

ROOT = pathlib.Path(__file__).resolve().parent.parent
PROVIDERS = json.loads((ROOT / "providers.json").read_text(encoding="utf-8"))
NOW = datetime.datetime.now(datetime.timezone.utc)


def load_rows(name="latest"):
    f = ROOT / "data" / "probes" / f"{name}.jsonl"
    if not f.exists():
        return []
    return [json.loads(l) for l in f.read_text(encoding="utf-8").splitlines() if l.strip()]


def pct(n, d):
    return "-" if d == 0 else f"{100.0 * n / d:.1f}%"


def p(vals, q):
    if not vals:
        return "-"
    vals = sorted(vals)
    k = max(0, min(len(vals) - 1, round(q * (len(vals) - 1))))
    return f"{vals[k] * 1000:.0f} ms"


def latest_row(rows, pid, kind, base):
    # 最新一轮里这家、这个端点、打到当前 base 的无 Key 样本（每轮只有一条）
    rs = [r for r in rows if r["provider"] == pid and r["kind"] == kind and not r["auth"]
          and r["url"].startswith(base.rstrip("/") + "/")]
    return rs[-1] if rs else None


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


def monitor_table(lang, rows):
    if lang == "zh":
        head = "| 服务商 | 端点 | 网关在线 | 端点有效 | 应答延迟 |\n|---|---|---|---|---|\n"
        yes, no, na = "是", "否", "-"
    else:
        head = "| Provider | Endpoint | Gateway up | Endpoint valid | Reject latency |\n|---|---|---|---|---|\n"
        yes, no, na = "yes", "no", "-"
    out = head
    for pr in PROVIDERS:
        for kind, label in (("anthropic", "/v1/messages"), ("openai", "/v1/chat/completions")):
            base = pr.get("anthropic_base" if kind == "anthropic" else "openai_base")
            if not base:
                continue
            r = latest_row(rows, pr["id"], kind, base)
            if r is None:
                out += f"| {pr['name']} | `{label}` | {na} | {na} | {na} |\n"
                continue
            up = yes if r["gateway_up"] else no
            valid = yes if r["endpoint_ok"] else f"{no} (HTTP {r['http']})" if r["gateway_up"] else no
            lat = f"{r['t_ttfb'] * 1000:.0f} ms" if r["gateway_up"] and r["t_ttfb"] > 0 else na
            out += f"| {pr['name']} | `{label}` | {up} | {valid} | {lat} |\n"
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
        # 节点顺序：国内在前（有数据才出），美国在后。每个节点各自一张最新一轮的表。
        vantages = [
            ("latest-cn", "国内节点（中国大陆，运营商宽带直连）", "China node (mainland broadband, direct)", "每 6 小时一轮，只展示最新一轮", "every 6 hours, latest round only"),
            ("latest", "海外节点（GitHub Actions，美国）", "Overseas node (GitHub Actions, US)", "每 6 小时一轮，只展示最新一轮", "every 6 hours, latest round only"),
        ]
        block = ""
        for name, zh_label, en_label, zh_tail, en_tail in vantages:
            rows = load_rows(name)
            if not rows:
                continue
            ts = rows[-1]["ts"].replace("T", " ").replace("Z", " UTC")
            if lang == "zh":
                block += f"### {zh_label}\n\n探测时间 {ts} · {zh_tail}\n\n" + monitor_table(lang, rows) + "\n"
            else:
                block += f"### {en_label}\n\nProbed {ts} · {en_tail}\n\n" + monitor_table(lang, rows) + "\n"
        text = splice(text, "MONITOR", block)
        path.write_text(text, encoding="utf-8")
        print("updated", fname)


if __name__ == "__main__":
    main()
