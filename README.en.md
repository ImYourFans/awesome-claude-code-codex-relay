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
| **302.AI** | [302.ai](https://302.ai) | [yes](https://help.302.ai/docs/jie-ru-dao-Claude-Code) | [yes](https://help.302.ai/docs/jie-ru-dao-Codex-CLI) | card, WeChat Pay | [pricing](https://302.ai/pricing) | open | Prepaid pay-as-you-go; Claude Code doc last edited 2025-07 with non-Claude example models | 2026-10-29 |
| **88code** | [www.88code.ai](https://www.88code.ai) | [yes](https://docs.88code.org/ClaudeCode/Windows.html) | [yes](https://docs.88code.org/Codex/Windows.html) | - | [pricing](https://docs.88code.org/88code/pricing.html) | open | Mainly monthly plans with daily quotas, plus pay-as-you-go packs; docs state at most 4 concurrent clients per account; 88code.org redirects to 88code.ai | 2026-10-29 |
| **AIHubMix** | [aihubmix.com](https://aihubmix.com) | [yes](https://docs.aihubmix.com/en/api/Claude-Code) | [yes](https://docs.aihubmix.com/cn/api/Codex-CLI) | card | [pricing](https://aihubmix.com/models) | open | Top-up via Stripe only, $15 minimum; backup domain api.inferera.com; Codex needs wire_api=responses | 2026-10-29 |
| **AnyRouter** | [anyrouter.top](https://anyrouter.top) | [yes](https://docs.anyrouter.top/) | no | - | - | unverified | Community (free) relay; docs say sign-up credits, no payment; registration page sits behind a CAPTCHA and the homepage could not be read | 2026-10-29 |
| **APIMart** | [apimart.ai](https://apimart.ai) | [yes](https://docs.apimart.ai/en/integrations/dev-tool/claude-code.md) | [yes](https://docs.apimart.ai/en/integrations/dev-tool/codex-cli.md) | card, Alipay, PayPal, crypto | [pricing](https://apimart.ai/pricing) | open | Pay-as-you-go with tiered member discounts; thinking variants use a -thinking suffix; Codex needs wire_api=responses | 2026-10-29 |
| **APINebula** | [apinebula.ai](https://apinebula.ai) | [yes](https://docs.apinebula.com/docs/cli/claude-code) | [yes](https://docs.apinebula.com/docs/cli/codex) | - | [pricing](https://apinebula.ai/zh/pricing) | open | Claude Code requires the 'Claude Code global' token group with an empty model list, else 403; Codex uses the CODEX group; homepage is client-rendered and payment methods could not be read from official pages | 2026-10-29 |
| **CloseAI** | [www.closeai-asia.com](https://www.closeai-asia.com) | [yes](https://doc.closeai-asia.com/tutorial/integrations/claude-code.html) | [yes](https://doc.closeai-asia.com/tutorial/integrations/codex-cli.html) | Alipay, WeChat Pay, card, bank transfer | [pricing](https://www.closeai-asia.com/pricing) | open | Priced as official price times a multiplier (1.1x to 1.5x tiers in docs); Anthropic protocol under /anthropic prefix, OpenAI-compatible under /v1 | 2026-10-29 |
| **CoderPlan** | [coderplan.ai](https://coderplan.ai) | [yes](https://coderplan.ai/docs/setup/claude-code) | [yes](https://coderplan.ai/docs/setup/codex-cli) | card | [pricing](https://coderplan.ai/pricing) | open | Pay-as-you-go, top-ups via Stripe, docs say no mainland China invoices yet; Codex needs wire_api=responses | 2026-10-29 |
| **DuckCoding** | [www.duckcoding.ai](https://www.duckcoding.ai) | [yes](https://docs.duckcoding.ai/) | [yes](https://docs.duckcoding.ai/) | - | [pricing](https://www.duckcoding.ai/pricing) | open | Site and docs are on the .ai domain; duckcoding.com showed an unbound-domain page on 2026-10-29; separate token groups for Claude Code and Codex; pay-as-you-go with per-group multipliers | 2026-10-29 |
| **laozhang.ai** | [www.laozhang.ai](https://www.laozhang.ai) | [yes](https://docs.laozhang.ai/en/scenarios/programming/claude-code) | [yes](https://docs.laozhang.ai/scenarios/programming/codex-cli.md) | card, bank transfer (business) | [pricing](https://docs.laozhang.ai/pricing.md) | open | Sign-up requires a Gmail address; docs say availability is subject to business whitelist review; Claude output capped at 32768 tokens | 2026-10-29 |
| **OhMyGPT** | [www.ohmygpt.com](https://www.ohmygpt.com) | [yes](https://docs.ohmygpt.com/docs/code-cli) | [yes](https://docs.ohmygpt.com/docs/code-cli) | Alipay, WeChat Pay, PayPal, card | [pricing](https://www.ohmygpt.com/models) | open | Official npx omgvibe writes Claude Code / Codex config; CDN mirror apic1.ohmycdn.com; homepage notice 2026-10-15 says the discounted Codex channel is discontinued | 2026-10-29 |
| **OpenRouter** | [openrouter.ai](https://openrouter.ai) | [yes](https://openrouter.ai/docs/guides/guides/claude-code-integration) | [yes](https://openrouter.ai/docs/cookbook/coding-agents/codex-cli) | card, Alipay, USDC | [pricing](https://openrouter.ai/pricing) | open | Model IDs carry a vendor prefix (anthropic/…); platform fee on credit purchases (5.5% Standard); Codex needs wire_api=responses | 2026-10-29 |
| **PackyAPI（原 PackyCode）** | [www.packyapi.com](https://www.packyapi.com) | [yes](https://docs.packyapi.com/docs/cli/2-claude.html) | [yes](https://docs.packyapi.com/docs/cli/3-codex.html) | Alipay, WeChat Pay | [pricing](https://www.packyapi.ai/pricing) | open | Separate token groups for Claude Code (CC) and Codex; docs also list slb-v1.api.fan; both packyapi.com and packyapi.ai are in use | 2026-10-29 |
| **QCode** | [qcode.cc](https://qcode.cc) | [yes](https://docs.qcode.cc/docs/getting-started/installation) | [yes](https://docs.qcode.cc/docs/ide/codex) | Alipay, WeChat Pay, card, Apple Pay, crypto | [pricing](https://qcode.cc/pricing) | open | Monthly plans with daily quotas plus 7-day pay-as-you-go packs; asia.qcode.cc endpoint recommended for mainland users; Claude models only via the Anthropic-style endpoint | 2026-10-29 |
| **TeamoRouter** (maintainer) | [teamorouter.com](https://teamorouter.com) | [yes](https://teamorouter.com/zh/docs/install-claude-code) | [yes](https://teamorouter.com/zh/docs/install-codex) | Alipay, card, USDT | [pricing](https://teamorouter.com/zh/pricing) | open | Pay-as-you-go; one key serves both the Anthropic-compatible and OpenAI-compatible endpoints; api.teamorouter.com is the global entry and api.teamorouter.cn the China entry, the probe hits the former; maintained by this repo's owner | 2026-10-29 |
| **YesCode** | [co.yes.vg](https://co.yes.vg) | no | no | - | - | unverified | Client-rendered site; docs and pricing are not readable statically; base URLs taken from the official setup-claude-code.sh and setup-codex.sh scripts (Codex uses wire_api=responses) | 2026-10-29 |
| **云雾AI** | [yunwu.ai](https://yunwu.ai) | [yes](https://s.apifox.cn/apidoc/docs-site/5427167/doc-7010249) | [yes](https://s.apifox.cn/apidoc/docs-site/5427167/doc-7422014) | - | - | open | Tokens must use the Claude Code group; default and reverse-engineered groups lack tool calling; Codex needs wire_api=responses; prices live inside the console and payment methods are not on public pages | 2026-10-29 |
| **灵眸AI** | [api.lmuai.ai](https://api.lmuai.ai) | [yes](https://docs.lmuai.ai/docs/tools/claude-code) | [yes](https://docs.lmuai.ai/docs/tools/codex-cli-mac) | - | [pricing](https://api.lmuai.ai/pricing) | open | Monthly plans split by Claude and GPT, plus balance-based pay-as-you-go; one key per group, cross-group calls return 400; docs warn proxies may drop streams | 2026-10-29 |
| **灵芽 API** | [api.lingyaai.cn](https://api.lingyaai.cn) | [yes](https://api.lingyaai.cn/aicoding.html#claude) | [yes](https://api.lingyaai.cn/aicoding.html#codex) | - | [pricing](https://api.lingyaai.cn/modellist/) | open | Separate groups for Claude Code / Codex / Gemini CLI; the official Claude Code example sets domestic models such as glm-5.2 and the FAQ model list shows no Claude model IDs | 2026-10-29 |
| **神马中转API** | [api.whatai.cc](https://api.whatai.cc) | [yes](https://docs.whatai.cc/docs/otherai/devtools/claudecode/) | [yes](https://docs.whatai.cc/docs/otherai/devtools/codex/) | Alipay, WeChat Pay, USDT | - | closed | Homepage on 2026-10-29 shows a closure and refund notice; docs remain online. Kept for reference, no longer probed | 2026-10-29 |
<!-- DIRECTORY:END -->

Rows are sorted by name, not ranked. "yes" in the Claude Code / Codex CLI columns links to that provider's own setup doc; "no" means we could not find one on their site, not that it does not work. Payments list only what the site states. To add or correct a row see [CONTRIBUTING.md](CONTRIBUTING.md).

## Availability probes

<!-- MONITOR:START -->
Last 7 days · updated 2026-10-29 13:32 UTC · vantage: GitHub Actions (US) · every 6 hours

| Provider | Endpoint | Samples | Gateway answered | Endpoint valid | Reject latency P50 | Reject latency P95 | Authenticated success |
|---|---|---|---|---|---|---|---|
| 302.AI | `/v1/messages` | 3 | 100.0% | 100.0% | 566 ms | 2737 ms | - |
| 302.AI | `/v1/chat/completions` | 3 | 100.0% | 100.0% | 565 ms | 1778 ms | - |
| 88code | `/v1/messages` | 3 | 100.0% | 100.0% | 667 ms | 705 ms | - |
| 88code | `/v1/chat/completions` | 3 | 100.0% | 100.0% | 529 ms | 613 ms | - |
| AIHubMix | `/v1/messages` | 3 | 100.0% | 100.0% | 159 ms | 180 ms | - |
| AIHubMix | `/v1/chat/completions` | 3 | 100.0% | 100.0% | 116 ms | 129 ms | - |
| AnyRouter | `/v1/messages` | 3 | 100.0% | 100.0% | 1565 ms | 1857 ms | - |
| APIMart | `/v1/messages` | 3 | 100.0% | 100.0% | 352 ms | 366 ms | - |
| APIMart | `/v1/chat/completions` | 3 | 100.0% | 100.0% | 295 ms | 303 ms | - |
| APINebula | `/v1/messages` | 3 | 100.0% | 100.0% | 210 ms | 215 ms | - |
| APINebula | `/v1/chat/completions` | 3 | 100.0% | 100.0% | 280 ms | 300 ms | - |
| CloseAI | `/v1/messages` | 3 | 100.0% | 100.0% | 264 ms | 272 ms | - |
| CloseAI | `/v1/chat/completions` | 3 | 100.0% | 100.0% | 116 ms | 133 ms | - |
| CoderPlan | `/v1/messages` | 3 | 100.0% | 100.0% | 704 ms | 712 ms | - |
| CoderPlan | `/v1/chat/completions` | 3 | 100.0% | 100.0% | 672 ms | 690 ms | - |
| DuckCoding | `/v1/messages` | 3 | 100.0% | 100.0% | 363 ms | 1151 ms | - |
| DuckCoding | `/v1/chat/completions` | 3 | 100.0% | 100.0% | 240 ms | 263 ms | - |
| laozhang.ai | `/v1/messages` | 3 | 100.0% | 100.0% | 178 ms | 340 ms | - |
| laozhang.ai | `/v1/chat/completions` | 3 | 100.0% | 100.0% | 152 ms | 217 ms | - |
| OhMyGPT | `/v1/messages` | 3 | 100.0% | 100.0% | 208 ms | 212 ms | - |
| OhMyGPT | `/v1/chat/completions` | 3 | 100.0% | 100.0% | 105 ms | 178 ms | - |
| OpenRouter | `/v1/messages` | 3 | 100.0% | 100.0% | 131 ms | 158 ms | - |
| OpenRouter | `/v1/chat/completions` | 3 | 100.0% | 100.0% | 67 ms | 74 ms | - |
| PackyAPI（原 PackyCode） | `/v1/messages` | 3 | 100.0% | 100.0% | 481 ms | 584 ms | - |
| PackyAPI（原 PackyCode） | `/v1/chat/completions` | 3 | 100.0% | 100.0% | 164 ms | 404 ms | - |
| QCode | `/v1/messages` | 3 | 100.0% | 100.0% | 349 ms | 388 ms | - |
| QCode | `/v1/chat/completions` | 3 | 100.0% | 100.0% | 312 ms | 383 ms | - |
| TeamoRouter | `/v1/messages` | 0 | - | - | - | - | - |
| TeamoRouter | `/v1/chat/completions` | 0 | - | - | - | - | - |
| YesCode | `/v1/messages` | 3 | 100.0% | 100.0% | 548 ms | 617 ms | - |
| YesCode | `/v1/chat/completions` | 3 | 100.0% | 100.0% | 504 ms | 582 ms | - |
| 云雾AI | `/v1/messages` | 3 | 100.0% | 100.0% | 465 ms | 484 ms | - |
| 云雾AI | `/v1/chat/completions` | 3 | 100.0% | 100.0% | 469 ms | 491 ms | - |
| 灵眸AI | `/v1/messages` | 3 | 100.0% | 100.0% | 780 ms | 802 ms | - |
| 灵眸AI | `/v1/chat/completions` | 3 | 100.0% | 100.0% | 561 ms | 636 ms | - |
| 灵芽 API | `/v1/messages` | 3 | 100.0% | 100.0% | 951 ms | 961 ms | - |
| 灵芽 API | `/v1/chat/completions` | 3 | 100.0% | 100.0% | 919 ms | 1210 ms | - |
| 神马中转API | `/v1/messages` | 0 | - | - | - | - | - |
| 神马中转API | `/v1/chat/completions` | 0 | - | - | - | - | - |
<!-- MONITOR:END -->

<details>
<summary>Last 30 days</summary>

<!-- MONITOR30:START -->
Last 30 days

| Provider | Endpoint | Samples | Gateway answered | Endpoint valid | Reject latency P50 | Reject latency P95 | Authenticated success |
|---|---|---|---|---|---|---|---|
| 302.AI | `/v1/messages` | 3 | 100.0% | 100.0% | 566 ms | 2737 ms | - |
| 302.AI | `/v1/chat/completions` | 3 | 100.0% | 100.0% | 565 ms | 1778 ms | - |
| 88code | `/v1/messages` | 3 | 100.0% | 100.0% | 667 ms | 705 ms | - |
| 88code | `/v1/chat/completions` | 3 | 100.0% | 100.0% | 529 ms | 613 ms | - |
| AIHubMix | `/v1/messages` | 3 | 100.0% | 100.0% | 159 ms | 180 ms | - |
| AIHubMix | `/v1/chat/completions` | 3 | 100.0% | 100.0% | 116 ms | 129 ms | - |
| AnyRouter | `/v1/messages` | 3 | 100.0% | 100.0% | 1565 ms | 1857 ms | - |
| APIMart | `/v1/messages` | 3 | 100.0% | 100.0% | 352 ms | 366 ms | - |
| APIMart | `/v1/chat/completions` | 3 | 100.0% | 100.0% | 295 ms | 303 ms | - |
| APINebula | `/v1/messages` | 3 | 100.0% | 100.0% | 210 ms | 215 ms | - |
| APINebula | `/v1/chat/completions` | 3 | 100.0% | 100.0% | 280 ms | 300 ms | - |
| CloseAI | `/v1/messages` | 3 | 100.0% | 100.0% | 264 ms | 272 ms | - |
| CloseAI | `/v1/chat/completions` | 3 | 100.0% | 100.0% | 116 ms | 133 ms | - |
| CoderPlan | `/v1/messages` | 3 | 100.0% | 100.0% | 704 ms | 712 ms | - |
| CoderPlan | `/v1/chat/completions` | 3 | 100.0% | 100.0% | 672 ms | 690 ms | - |
| DuckCoding | `/v1/messages` | 3 | 100.0% | 100.0% | 363 ms | 1151 ms | - |
| DuckCoding | `/v1/chat/completions` | 3 | 100.0% | 100.0% | 240 ms | 263 ms | - |
| laozhang.ai | `/v1/messages` | 3 | 100.0% | 100.0% | 178 ms | 340 ms | - |
| laozhang.ai | `/v1/chat/completions` | 3 | 100.0% | 100.0% | 152 ms | 217 ms | - |
| OhMyGPT | `/v1/messages` | 3 | 100.0% | 100.0% | 208 ms | 212 ms | - |
| OhMyGPT | `/v1/chat/completions` | 3 | 100.0% | 100.0% | 105 ms | 178 ms | - |
| OpenRouter | `/v1/messages` | 3 | 100.0% | 100.0% | 131 ms | 158 ms | - |
| OpenRouter | `/v1/chat/completions` | 3 | 100.0% | 100.0% | 67 ms | 74 ms | - |
| PackyAPI（原 PackyCode） | `/v1/messages` | 3 | 100.0% | 100.0% | 481 ms | 584 ms | - |
| PackyAPI（原 PackyCode） | `/v1/chat/completions` | 3 | 100.0% | 100.0% | 164 ms | 404 ms | - |
| QCode | `/v1/messages` | 3 | 100.0% | 100.0% | 349 ms | 388 ms | - |
| QCode | `/v1/chat/completions` | 3 | 100.0% | 100.0% | 312 ms | 383 ms | - |
| TeamoRouter | `/v1/messages` | 0 | - | - | - | - | - |
| TeamoRouter | `/v1/chat/completions` | 0 | - | - | - | - | - |
| YesCode | `/v1/messages` | 3 | 100.0% | 100.0% | 548 ms | 617 ms | - |
| YesCode | `/v1/chat/completions` | 3 | 100.0% | 100.0% | 504 ms | 582 ms | - |
| 云雾AI | `/v1/messages` | 3 | 100.0% | 100.0% | 465 ms | 484 ms | - |
| 云雾AI | `/v1/chat/completions` | 3 | 100.0% | 100.0% | 469 ms | 491 ms | - |
| 灵眸AI | `/v1/messages` | 3 | 100.0% | 100.0% | 780 ms | 802 ms | - |
| 灵眸AI | `/v1/chat/completions` | 3 | 100.0% | 100.0% | 561 ms | 636 ms | - |
| 灵芽 API | `/v1/messages` | 3 | 100.0% | 100.0% | 951 ms | 961 ms | - |
| 灵芽 API | `/v1/chat/completions` | 3 | 100.0% | 100.0% | 919 ms | 1210 ms | - |
| 神马中转API | `/v1/messages` | 0 | - | - | - | - | - |
| 神马中转API | `/v1/chat/completions` | 0 | - | - | - | - | - |
<!-- MONITOR30:END -->

</details>

### Method

- Script: [`scripts/probe.py`](scripts/probe.py); raw data: [`data/probes/`](data/probes/), one JSON object per line.
- **Unauthenticated probe** (every provider): a minimal request with a dummy key to `anthropic_base/v1/messages` and `openai_base/v1/chat/completions`.
  - **Gateway answered**: curl got any HTTP response below 500.
  - **Endpoint valid**: the response was 400 / 401 / 403 / 422 / 429, i.e. the endpoint exists and validated the request. 404 / 405 count as gateway up but wrong path.
  - **Reject latency**: time from sending the request to the gateway's rejection (usually 401), P50 / P95 over samples where the gateway answered. It measures network distance from the probe node plus the gateway's auth overhead. It is **not** model time-to-first-token and involves no inference.
- **Authenticated probe** (only TeamoRouter, the maintainer's own key): a real request with `max_tokens=8`; success means HTTP 200 and "ok" in the reply. `-` for other providers means not tested, not failed.
- The vantage point is a GitHub Actions runner in the US. **This measures reachability and latency from overseas, not the experience inside China.** Run the same script elsewhere (`PROBE_VANTAGE=<region> python3 scripts/probe.py`) and open a PR with the results.
- One sample per run, four runs a day. Percentages swing with few samples; the 30-day table is steadier.

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
