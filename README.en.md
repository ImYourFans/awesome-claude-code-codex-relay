# awesome-claude-code-codex-relay

A directory of API relays (proxies) for Claude Code and Codex CLI, with automated availability probes every 6 hours. [中文](README.md)

[![probe](https://github.com/zhaoshengxiong/awesome-claude-code-codex-relay/actions/workflows/probe.yml/badge.svg)](https://github.com/zhaoshengxiong/awesome-claude-code-codex-relay/actions/workflows/probe.yml)
![license](https://img.shields.io/badge/license-MIT-green)

> **Disclosure**: this repository is maintained by the [TeamoRouter](https://teamorouter.com) team, and TeamoRouter is one of the providers listed. We do not rate, rank or review anyone. The table holds only facts you can check on each provider's own site and numbers produced by the probe script. The script and raw data are in this repo; run them yourself, against us included. No affiliate links or invite codes.

## Why this exists

Using the Anthropic and OpenAI APIs directly from mainland China (and some other regions) runs into account, payment and network problems, so people route through a relay. There are many relays, information is scattered and changes fast, and most "recommendation lists" are either affiliate-driven or written by one of the relays. This repo does two things only:

1. **Directory**: each provider's website, whether it publishes Claude Code and Codex setup docs, payment methods, pricing page, sign-up status, with a verification date and sources per row.
2. **Availability probes**: GitHub Actions hits every provider's API endpoints every 6 hours and records whether the gateway answered, whether the endpoint is valid, and how fast it rejects an unauthenticated request.

Not done here: judging model authenticity (see "Verify a relay yourself"), comparing prices (every provider quotes differently; read their pricing page), star ratings.

## Directory

<!-- DIRECTORY:START -->
| Provider | Website | Claude Code | Codex CLI | Payments | Pricing | Sign-up | Notes | Verified |
|---|---|---|---|---|---|---|---|---|
| **88code** | [www.88code.ai](https://www.88code.ai) | [yes](https://docs.88code.org/ClaudeCode/Windows.html) | [yes](https://docs.88code.org/Codex/Windows.html) | - | [pricing](https://docs.88code.org/88code/pricing.html) | open | Mainly monthly plans with daily quotas, plus pay-as-you-go packs; docs state at most 4 concurrent clients per account; 88code.org redirects to 88code.ai | 2026-10-29 |
| **AnyRouter** | [anyrouter.top](https://anyrouter.top) | [yes](https://docs.anyrouter.top/) | no | - | - | unverified | Community (free) relay; docs say sign-up credits, no payment; registration page sits behind a CAPTCHA and the homepage could not be read | 2026-10-29 |
| **CoderPlan** | [coderplan.ai](https://coderplan.ai) | [yes](https://coderplan.ai/docs/setup/claude-code) | [yes](https://coderplan.ai/docs/setup/codex-cli) | card | [pricing](https://coderplan.ai/pricing) | open | Pay-as-you-go, top-ups via Stripe, docs say no mainland China invoices yet; Codex needs wire_api=responses | 2026-10-29 |
| **DuckCoding** | [www.duckcoding.ai](https://www.duckcoding.ai) | [yes](https://docs.duckcoding.ai/) | [yes](https://docs.duckcoding.ai/) | - | [pricing](https://www.duckcoding.ai/pricing) | open | Site and docs are on the .ai domain; duckcoding.com showed an unbound-domain page on 2026-10-29; separate token groups for Claude Code and Codex; pay-as-you-go with per-group multipliers | 2026-10-29 |
| **OhMyGPT** | [www.ohmygpt.com](https://www.ohmygpt.com) | [yes](https://docs.ohmygpt.com/docs/code-cli) | [yes](https://docs.ohmygpt.com/docs/code-cli) | Alipay, WeChat Pay, PayPal, card | [pricing](https://www.ohmygpt.com/models) | open | Official npx omgvibe writes Claude Code / Codex config; CDN mirror apic1.ohmycdn.com; homepage notice 2026-10-15 says the discounted Codex channel is discontinued | 2026-10-29 |
| **OpenRouter** | [openrouter.ai](https://openrouter.ai) | [yes](https://openrouter.ai/docs/guides/guides/claude-code-integration) | [yes](https://openrouter.ai/docs/cookbook/coding-agents/codex-cli) | card, Alipay, USDC | [pricing](https://openrouter.ai/pricing) | open | Model IDs carry a vendor prefix (anthropic/…); platform fee on credit purchases (5.5% Standard); Codex needs wire_api=responses | 2026-10-29 |
| **PackyAPI（原 PackyCode）** | [www.packyapi.com](https://www.packyapi.com) | [yes](https://docs.packyapi.com/docs/cli/2-claude.html) | [yes](https://docs.packyapi.com/docs/cli/3-codex.html) | Alipay, WeChat Pay | [pricing](https://www.packyapi.ai/pricing) | open | Separate token groups for Claude Code (CC) and Codex; docs also list slb-v1.api.fan; both packyapi.com and packyapi.ai are in use | 2026-10-29 |
| **TeamoRouter** (maintainer) | [teamorouter.com](https://teamorouter.com) | [yes](https://teamorouter.com/zh/docs/install-claude-code) | [yes](https://teamorouter.com/zh/docs/install-codex) | Alipay, card, USDT | [pricing](https://teamorouter.com/zh/pricing) | open | Pay-as-you-go; one key serves both the Anthropic-compatible and OpenAI-compatible endpoints; api.teamorouter.com is the global entry and api.teamorouter.cn the China entry, the probe hits the former; maintained by this repo's owner | 2026-10-29 |
| **YesCode** | [co.yes.vg](https://co.yes.vg) | no | no | - | - | unverified | Client-rendered site; docs and pricing are not readable statically; base URLs taken from the official setup-claude-code.sh and setup-codex.sh scripts (Codex uses wire_api=responses) | 2026-10-29 |
| **灵芽 API** | [api.lingyaai.cn](https://api.lingyaai.cn) | [yes](https://api.lingyaai.cn/aicoding.html#claude) | [yes](https://api.lingyaai.cn/aicoding.html#codex) | - | [pricing](https://api.lingyaai.cn/modellist/) | open | Separate groups for Claude Code / Codex / Gemini CLI; the official Claude Code example sets domestic models such as glm-5.2 and the FAQ model list shows no Claude model IDs | 2026-10-29 |
<!-- DIRECTORY:END -->

Rows are sorted by name, not ranked. "yes" in the Claude Code / Codex CLI columns links to that provider's own setup doc; "no" means we could not find one on their site, not that it does not work. Payments list only what the site states. To add or correct a row see [CONTRIBUTING.md](CONTRIBUTING.md).

## Availability probes

<!-- MONITOR:START -->
Latest round · probed 2026-10-29 14:55:47 UTC · vantage: GitHub Actions (US) · every 6 hours, latest round only

| Provider | Endpoint | Gateway up | Endpoint valid | Reject latency |
|---|---|---|---|---|
| 88code | `/v1/messages` | yes | yes | 715 ms |
| 88code | `/v1/chat/completions` | yes | yes | 683 ms |
| AnyRouter | `/v1/messages` | yes | yes | 1219 ms |
| CoderPlan | `/v1/messages` | yes | yes | 837 ms |
| CoderPlan | `/v1/chat/completions` | yes | yes | 725 ms |
| DuckCoding | `/v1/messages` | yes | yes | 1061 ms |
| DuckCoding | `/v1/chat/completions` | yes | yes | 1078 ms |
| OhMyGPT | `/v1/messages` | yes | yes | 243 ms |
| OhMyGPT | `/v1/chat/completions` | yes | yes | 166 ms |
| OpenRouter | `/v1/messages` | yes | yes | 91 ms |
| OpenRouter | `/v1/chat/completions` | yes | yes | 50 ms |
| PackyAPI（原 PackyCode） | `/v1/messages` | yes | yes | 470 ms |
| PackyAPI（原 PackyCode） | `/v1/chat/completions` | yes | yes | 127 ms |
| TeamoRouter | `/v1/messages` | yes | yes | 682 ms |
| TeamoRouter | `/v1/chat/completions` | yes | yes | 855 ms |
| YesCode | `/v1/messages` | yes | yes | 414 ms |
| YesCode | `/v1/chat/completions` | yes | yes | 431 ms |
| 灵芽 API | `/v1/messages` | yes | yes | 1056 ms |
| 灵芽 API | `/v1/chat/completions` | yes | yes | 1003 ms |
<!-- MONITOR:END -->


### Method

- Script: [`scripts/probe.py`](scripts/probe.py); raw data: [`data/probes/latest.jsonl`](data/probes/latest.jsonl), one JSON object per line. Overwritten every run; the repo keeps only the latest round, no history.
- **Unauthenticated probe** (every provider): a minimal request with a dummy key to `anthropic_base/v1/messages` and `openai_base/v1/chat/completions`.
  - **Gateway answered**: curl got any HTTP response below 500.
  - **Endpoint valid**: the response was 400 / 401 / 403 / 422 / 429, i.e. the endpoint exists and validated the request. 404 / 405 count as gateway up but wrong path.
  - **Reject latency**: time from sending the request to the gateway's rejection (usually 401). It measures network distance from the probe node plus the gateway's auth overhead. It is **not** model time-to-first-token and involves no inference.
- **Authenticated probe** (only TeamoRouter, whose key the maintainer has): one extra real request per run (`max_tokens=8`, `claude-haiku-5-5` on the Anthropic endpoint, `gpt-6.1-terra` on the OpenAI endpoint). Results live only in the raw data (including the response's `model` field) and are not in the table above.
- The vantage point is a GitHub Actions runner in the US. **This measures reachability and latency from overseas, not the experience inside China.** Run the same script elsewhere (`PROBE_VANTAGE=<region> python3 scripts/probe.py`) and open a PR with the results.
- One round every 6 hours; the table shows only the latest round, so single readings will fluctuate. Run the script yourself on a schedule if you want a trend.

## Verify a relay yourself

Whatever the table says, spend five minutes on these before committing:

1. **Is the model real**: request `claude-opus-5-5`, check the `model` field in the response, then compare an answer with a known solution against the official API.
2. **Is prompt caching billed**: most of a Claude Code session's input is repeated context billed at cache rates. A bill with cache reads stuck at zero means the same work costs several times more.
3. **Start small**: top up the minimum, run a day, read the itemised bill.

Minimal endpoint check (replace the base URL and key):

```bash
curl -sS https://<anthropic_base>/v1/messages \
  -H "x-api-key: $KEY" -H "anthropic-version: 2023-06-01" -H "content-type: application/json" \
  -d '{"model":"claude-opus-5-5","max_tokens":8,"messages":[{"role":"user","content":"Reply with the single word: ok"}]}'
```

## Setup

### Claude Code

```bash
export ANTHROPIC_BASE_URL=https://<anthropic_base>
export ANTHROPIC_AUTH_TOKEN=<your key>
claude
```

Some relays want `ANTHROPIC_API_KEY` instead of `ANTHROPIC_AUTH_TOKEN`; setting both conflicts, follow the provider's doc. Model IDs usually match the official ones (`claude-opus-5-5`, `claude-sonnet-5-5`); a few providers map their own.

### Codex CLI

`~/.codex/config.toml`:

```toml
model_provider = "relay"
model = "gpt-6-sol"

[model_providers.relay]
name = "relay"
base_url = "https://<openai_base>/v1"
env_key = "RELAY_API_KEY"
wire_api = "responses"
```

Then `export RELAY_API_KEY=<your key>`. `wire_api` must match what the relay supports: `responses` if it serves `/v1/responses`, `chat` if it only serves `/v1/chat/completions`.

## Contributing

Additions and corrections go through PRs, see [CONTRIBUTING.md](CONTRIBUTING.md): a source URL for every field, facts only in `notes`, disclose if you represent the provider, no affiliate links.

## Disclaimer

This repository aggregates public information and automated probe results. It makes no claims about any provider's service quality, model authenticity or financial safety. A probe result describes what the probe node saw at that moment.

---

Keywords: Claude Code relay, Codex relay, Claude API proxy, OpenAI API proxy, Codex CLI China, Claude Code China, API relay, ANTHROPIC_BASE_URL, relay uptime monitor, awesome claude code, awesome codex
