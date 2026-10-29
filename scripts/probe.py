#!/usr/bin/env python3
"""Probe every provider in providers.json and append one JSON line per (provider, endpoint) to data/probes/YYYY-MM.jsonl.

Two kinds of probe:
- unauthenticated (all providers): POST a minimal body with a dummy key. Any HTTP reply below 500
  means the gateway answered; 400/401/403/422/429 means the endpoint exists and validated the request.
- authenticated (only providers whose key is present in env as KEY_<ID>): a real request with
  max_tokens=8. Only the maintainer's own key is configured; this is stated in the README.
Timings come from curl: t_tls = time to TLS handshake, t_ttfb = time to first byte, t_total.
"""
import json, os, subprocess, sys, datetime, pathlib, tempfile

ROOT = pathlib.Path(__file__).resolve().parent.parent
PROVIDERS = json.loads((ROOT / "providers.json").read_text(encoding="utf-8"))
NOW = datetime.datetime.now(datetime.timezone.utc)
OUT = ROOT / "data" / "probes" / f"{NOW:%Y-%m}.jsonl"
OUT.parent.mkdir(parents=True, exist_ok=True)
VANTAGE = os.environ.get("PROBE_VANTAGE", "github-actions")
PROMPT = "Reply with the single word: ok"
TIMEOUT = int(os.environ.get("PROBE_TIMEOUT", "30"))
ENDPOINT_OK = {200, 400, 401, 403, 422, 429}


def curl(url, headers, body):
    with tempfile.NamedTemporaryFile(delete=False) as tmp:
        tmp_path = tmp.name
    cmd = ["curl", "-sS", "-m", str(TIMEOUT), "-o", tmp_path,
           "-w", "%{http_code},%{time_appconnect},%{time_starttransfer},%{time_total}", url,
           "-H", "content-type: application/json", "-H", "anthropic-version: 2023-06-01",
           "-A", "awesome-claude-code-codex-relay-probe/1.0 (+https://github.com/zhaoshengxiong/awesome-claude-code-codex-relay)"]
    for h in headers:
        cmd += ["-H", h]
    cmd += ["-d", json.dumps(body)]
    p = subprocess.run(cmd, capture_output=True, text=True)
    w = p.stdout.strip() or "000,0,0,0"
    http, tls, ttfb, total = w.split(",")[:4]
    try:
        resp = pathlib.Path(tmp_path).read_text(encoding="utf-8", errors="replace")
    except Exception:
        resp = ""
    os.unlink(tmp_path)
    return int(http), p.returncode, float(tls), float(ttfb), float(total), resp, (p.stderr or "").strip()


def record(provider, kind, endpoint, url, auth, http, rc, tls, ttfb, total, resp, err):
    gateway_up = rc == 0 and 0 < http < 500
    endpoint_ok = rc == 0 and http in ENDPOINT_OK
    ok = None
    note = ""
    if auth:
        ok = rc == 0 and http == 200 and "ok" in resp.lower()
    if not (gateway_up and endpoint_ok) or (auth and not ok):
        note = (err or resp).replace("\n", " ")[:160]
    row = {"ts": NOW.strftime("%Y-%m-%dT%H:%M:%SZ"), "vantage": VANTAGE, "provider": provider["id"],
           "kind": kind, "endpoint": endpoint, "url": url, "auth": auth, "http": http, "curl_exit": rc,
           "t_tls": round(tls, 3), "t_ttfb": round(ttfb, 3), "t_total": round(total, 3),
           "gateway_up": gateway_up, "endpoint_ok": endpoint_ok, "ok": ok, "note": note}
    with OUT.open("a", encoding="utf-8") as f:
        f.write(json.dumps(row, ensure_ascii=False) + "\n")
    print(f"{row['ts']} {provider['id']:<14} {endpoint:<10} auth={int(auth)} http={http} rc={rc} ttfb={ttfb:.2f}s {note[:60]}")


def probe_provider(p):
    key = os.environ.get("KEY_" + p["id"].upper().replace("-", "_"))
    if p.get("anthropic_base"):
        url = p["anthropic_base"].rstrip("/") + "/v1/messages"
        model = (p.get("claude_models_claimed") or ["claude-sonnet-5-5"])[0]
        body = {"model": model, "max_tokens": 8, "messages": [{"role": "user", "content": PROMPT}]}
        record(p, "anthropic", "messages", url, False, *curl(url, ["x-api-key: probe-no-key"], body))
        if key:
            record(p, "anthropic", "messages", url, True, *curl(url, [f"x-api-key: {key}"], body))
    if p.get("openai_base"):
        url = p["openai_base"].rstrip("/") + "/v1/chat/completions"
        model = (p.get("openai_models_claimed") or ["gpt-6-sol"])[0]
        body = {"model": model, "max_tokens": 8, "messages": [{"role": "user", "content": PROMPT}]}
        record(p, "openai", "chat", url, False, *curl(url, ["Authorization: Bearer probe-no-key"], body))
        if key:
            record(p, "openai", "chat", url, True, *curl(url, [f"Authorization: Bearer {key}"], body))


def main():
    only = sys.argv[1:]  # optional provider ids
    for p in PROVIDERS:
        if only and p["id"] not in only:
            continue
        if p.get("registration") == "closed" and not p.get("probe_anyway"):
            continue
        try:
            probe_provider(p)
        except Exception as e:  # never let one provider abort the run
            print(f"!! {p['id']}: {e}", file=sys.stderr)


if __name__ == "__main__":
    main()
