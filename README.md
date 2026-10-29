# awesome-claude-code-codex-relay

Claude Code / Codex CLI 中转站（API relay）导航，附每 6 小时一轮的自动可用性探测。[English](README.en.md)

[![probe](https://github.com/zhaoshengxiong/awesome-claude-code-codex-relay/actions/workflows/probe.yml/badge.svg)](https://github.com/zhaoshengxiong/awesome-claude-code-codex-relay/actions/workflows/probe.yml)
![license](https://img.shields.io/badge/license-MIT-green)

> **利益相关声明**：本仓库由 [TeamoRouter](https://teamorouter.com) 团队维护，TeamoRouter 也是下表里的一家。我们不给任何一家打星、排名或写评价，表里只有能在各家官网核对的事实和脚本自动测出来的数字。探测脚本、原始数据都在仓库里，你可以自己跑一遍复核，包括对我们自己。表里没有返利链接和邀请码。

## 这个仓库解决什么问题

国内直接用 Anthropic 和 OpenAI 官方 API 卡在账号、付款和网络三件事上，常见做法是接一个中转站。中转站很多，信息散、变化快，而且大多数「推荐榜」要么是返利驱动，要么是某一家自己写的。这里只做两件事：

1. **导航表**：每家的官网、是否有 Claude Code 和 Codex 的接入文档、支付方式、价格页、是否还开放注册，每条都标核实日期和来源。
2. **可用性探测**：GitHub Actions 每 6 小时对每家的 API 端点发一次请求，记录网关有没有应答、端点是否有效、首字节延迟。

不做的事：不评价模型真伪（见下文「自己怎么验」），不比较价格（各家口径不一致，自己去价格页看），不打星。

## 导航表

<!-- DIRECTORY:START -->
| 服务商 | 官网 | Claude Code | Codex CLI | 支付方式 | 价格页 | 注册 | 备注 | 核实日期 |
|---|---|---|---|---|---|---|---|---|
| **88code** | [www.88code.ai](https://www.88code.ai) | [是](https://docs.88code.org/ClaudeCode/Windows.html) | [是](https://docs.88code.org/Codex/Windows.html) | - | [价格](https://docs.88code.org/88code/pricing.html) | 开放 | 以包月套餐为主（按日额度），另有按量包；文档写每账号最多 4 个客户端并发；88code.org 跳转到 88code.ai | 2026-10-29 |
| **AnyRouter** | [anyrouter.top](https://anyrouter.top) | [是](https://docs.anyrouter.top/) | 否 | - | - | 未核实 | 公益站，官方文档称注册赠送额度、不需付款；注册页有人机验证，官网首页无法抓取文本 | 2026-10-29 |
| **CoderPlan** | [coderplan.ai](https://coderplan.ai) | [是](https://coderplan.ai/docs/setup/claude-code) | [是](https://coderplan.ai/docs/setup/codex-cli) | 信用卡 | [价格](https://coderplan.ai/pricing) | 开放 | 按量付费，充值走 Stripe，文档称暂不支持国内发票；Codex 需 wire_api=responses | 2026-10-29 |
| **DuckCoding** | [www.duckcoding.ai](https://www.duckcoding.ai) | [是](https://docs.duckcoding.ai/) | [是](https://docs.duckcoding.ai/) | - | [价格](https://www.duckcoding.ai/pricing) | 开放 | 官网与文档在 .ai 域名，duckcoding.com 2026-10-29 显示域名未绑定；需分别创建 Claude Code 专用和 Codex 专用分组令牌；按量计费，各分组另乘倍率 | 2026-10-29 |
| **OhMyGPT** | [www.ohmygpt.com](https://www.ohmygpt.com) | [是](https://docs.ohmygpt.com/docs/code-cli) | [是](https://docs.ohmygpt.com/docs/code-cli) | 支付宝、微信、PayPal、信用卡 | [价格](https://www.ohmygpt.com/models) | 开放 | 官方推荐 npx omgvibe 一键写入 Claude Code / Codex 配置；另有 CDN 镜像域名 apic1.ohmycdn.com；首页公告 2026-10-15 称 Codex 折扣渠道已停用 | 2026-10-29 |
| **OpenRouter** | [openrouter.ai](https://openrouter.ai) | [是](https://openrouter.ai/docs/guides/guides/claude-code-integration) | [是](https://openrouter.ai/docs/cookbook/coding-agents/codex-cli) | 信用卡、支付宝、USDC | [价格](https://openrouter.ai/pricing) | 开放 | 模型 ID 带厂商前缀（anthropic/…）；购买额度收平台费（Standard 5.5%）；Codex 需 wire_api=responses | 2026-10-29 |
| **PackyAPI（原 PackyCode）** | [www.packyapi.com](https://www.packyapi.com) | [是](https://docs.packyapi.com/docs/cli/2-claude.html) | [是](https://docs.packyapi.com/docs/cli/3-codex.html) | 支付宝、微信 | [价格](https://www.packyapi.ai/pricing) | 开放 | Claude Code 和 Codex 要分别用 CC 分组和 Codex 分组的令牌；文档另给优化线路 slb-v1.api.fan；官网 packyapi.com 与 packyapi.ai 并存 | 2026-10-29 |
| **TeamoRouter**（本仓库维护者） | [teamorouter.com](https://teamorouter.com) | [是](https://teamorouter.com/zh/docs/install-claude-code) | [是](https://teamorouter.com/zh/docs/install-codex) | 支付宝、信用卡、USDT | [价格](https://teamorouter.com/zh/pricing) | 开放 | 按量计费；同一个 Key 同时走 Anthropic 兼容和 OpenAI 兼容端点；海外入口 api.teamorouter.com，国内入口 api.teamorouter.cn，本表从海外节点探前者；本仓库维护者 | 2026-10-29 |
| **YesCode** | [co.yes.vg](https://co.yes.vg) | 否 | 否 | - | - | 未核实 | 官网为纯前端应用，文档和价格页需站内渲染；Base URL 取自官方脚本 setup-claude-code.sh 和 setup-codex.sh（Codex 用 wire_api=responses） | 2026-10-29 |
| **灵芽 API** | [api.lingyaai.cn](https://api.lingyaai.cn) | [是](https://api.lingyaai.cn/aicoding.html#claude) | [是](https://api.lingyaai.cn/aicoding.html#codex) | - | [价格](https://api.lingyaai.cn/modellist/) | 开放 | Claude Code / Codex / Gemini CLI 各有专用分组；官方 Claude Code 示例配置的是 glm-5.2 等国产模型，FAQ 模型列表未出现 Claude 模型 ID | 2026-10-29 |
<!-- DIRECTORY:END -->

表按名称排序，不是排名。「Claude Code / Codex CLI」列里的「是」链接到该家自己的接入文档；「否」表示我们在官网没找到对应文档，不代表不能用。支付方式只写官网明确列出的。想补充或更正，见 [CONTRIBUTING.md](CONTRIBUTING.md)。

## 可用性探测

<!-- MONITOR:START -->
最新一轮 · 探测时间 2026-10-29 14:55:47 UTC · 探测节点：GitHub Actions（美国）· 每 6 小时一轮，只展示最新一轮

| 服务商 | 端点 | 网关在线 | 端点有效 | 应答延迟 |
|---|---|---|---|---|
| 88code | `/v1/messages` | 是 | 是 | 715 ms |
| 88code | `/v1/chat/completions` | 是 | 是 | 683 ms |
| AnyRouter | `/v1/messages` | 是 | 是 | 1219 ms |
| CoderPlan | `/v1/messages` | 是 | 是 | 837 ms |
| CoderPlan | `/v1/chat/completions` | 是 | 是 | 725 ms |
| DuckCoding | `/v1/messages` | 是 | 是 | 1061 ms |
| DuckCoding | `/v1/chat/completions` | 是 | 是 | 1078 ms |
| OhMyGPT | `/v1/messages` | 是 | 是 | 243 ms |
| OhMyGPT | `/v1/chat/completions` | 是 | 是 | 166 ms |
| OpenRouter | `/v1/messages` | 是 | 是 | 91 ms |
| OpenRouter | `/v1/chat/completions` | 是 | 是 | 50 ms |
| PackyAPI（原 PackyCode） | `/v1/messages` | 是 | 是 | 470 ms |
| PackyAPI（原 PackyCode） | `/v1/chat/completions` | 是 | 是 | 127 ms |
| TeamoRouter | `/v1/messages` | 是 | 是 | 682 ms |
| TeamoRouter | `/v1/chat/completions` | 是 | 是 | 855 ms |
| YesCode | `/v1/messages` | 是 | 是 | 414 ms |
| YesCode | `/v1/chat/completions` | 是 | 是 | 431 ms |
| 灵芽 API | `/v1/messages` | 是 | 是 | 1056 ms |
| 灵芽 API | `/v1/chat/completions` | 是 | 是 | 1003 ms |
<!-- MONITOR:END -->


### 监控方法

- 脚本：[`scripts/probe.py`](scripts/probe.py)，原始数据：[`data/probes/latest.jsonl`](data/probes/latest.jsonl)，每行一条 JSON。每轮覆盖，仓库只保留最新一轮，不存历史。
- **无 Key 探测**（所有家）：向 `anthropic_base/v1/messages` 和 `openai_base/v1/chat/completions` 各发一个带假 Key 的最小请求。
  - **网关在线**：curl 拿到任何 5xx 以下的 HTTP 响应，说明网关在线。
  - **端点有效**：响应是 400 / 401 / 403 / 422 / 429 之一，说明端点存在并且校验了请求。404 或 405 算网关在线但端点路径不对。
  - **应答延迟**：从发起请求到网关返回拒绝（通常是 401）的时间。它量的是节点到网关的网络距离加网关鉴权的开销，**不是模型首字延迟**，不包含任何推理。
- **认证探测**（只有维护者自己有 Key 的 TeamoRouter）：每轮另发一个真实请求（`max_tokens=8`，Anthropic 端点 `claude-haiku-5-5`，OpenAI 端点 `gpt-6.1-terra`），结果只记在原始数据里（含回包 `model` 字段），不进上表。
- 节点在 GitHub Actions 的美国机房，**反映的是海外到各家网关的可达性和延迟，不等于国内体验**。想要国内节点的数据，可以在自己机器上跑同一脚本（`PROBE_VANTAGE=cn-xxx python3 scripts/probe.py`）并提 PR。
- 每 6 小时一轮，表里只放最新一轮的结果，单次数值会有波动，看趋势请自己定期跑脚本。

## 自己怎么验一家中转站

不管表里怎么写，接入前花 5 分钟当场验这三件事：

1. **模型是不是真的**：请求 `claude-opus-5-5`，看回包 `model` 字段是不是它，再拿一道有标准答案的题对比官方回答。
2. **缓存有没有正常计费**：Claude Code 一个会话里大部分输入是重复发送的上下文，走缓存价。账单里缓存读写一直是 0 的平台，同样的活会贵好几倍。
3. **先小额**：充最低档跑一天，看账单明细再决定。

验端点能不能通的最小命令（把 Base URL 和 Key 换成你的）：

```bash
curl -sS https://<anthropic_base>/v1/messages \
  -H "x-api-key: $KEY" -H "anthropic-version: 2023-06-01" -H "content-type: application/json" \
  -d '{"model":"claude-opus-5-5","max_tokens":8,"messages":[{"role":"user","content":"Reply with the single word: ok"}]}'
```

## 接入配置

### Claude Code

```bash
export ANTHROPIC_BASE_URL=https://<anthropic_base>
export ANTHROPIC_AUTH_TOKEN=<你的 Key>
claude
```

有的中转站要求用 `ANTHROPIC_API_KEY` 而不是 `ANTHROPIC_AUTH_TOKEN`，两者同时设会冲突，以该家文档为准。模型 ID 一般和官方一致（`claude-opus-5-5`、`claude-sonnet-5-5`），少数家有自己的映射。

### Codex CLI

`~/.codex/config.toml`：

```toml
model_provider = "relay"
model = "gpt-6-sol"

[model_providers.relay]
name = "relay"
base_url = "https://<openai_base>/v1"
env_key = "RELAY_API_KEY"
wire_api = "responses"
```

然后 `export RELAY_API_KEY=<你的 Key>`。`wire_api` 要和该家支持的接口一致：支持 `/v1/responses` 的填 `responses`，只支持 `/v1/chat/completions` 的填 `chat`。

## 贡献

新增、更正都走 PR，要求见 [CONTRIBUTING.md](CONTRIBUTING.md)：每个字段要有来源 URL，`notes` 只写事实，代表服务商的请说明，不收返利链接。

## 免责声明

本仓库只汇总公开信息和自动探测结果，不对任何服务商的服务质量、模型真实性、资金安全负责。探测结果只说明探测时刻从探测节点看到的状态。

---

关键词：Claude Code 中转站, Codex 中转, Claude API 中转, Claude API 代理, OpenAI API 中转, Codex CLI 国内, Claude Code 国内, API relay, API proxy, ANTHROPIC_BASE_URL, 中转站可用性监控, awesome claude code, awesome codex
