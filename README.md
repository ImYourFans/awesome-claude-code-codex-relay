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
| **302.AI** | [302.ai](https://302.ai) | [是](https://help.302.ai/docs/jie-ru-dao-Claude-Code) | [是](https://help.302.ai/docs/jie-ru-dao-Codex-CLI) | 信用卡、微信 | [价格](https://302.ai/pricing) | 开放 | 预充值按量扣费；Claude Code 文档最近修改 2025-07，示例模型非 Claude | 2026-10-29 |
| **88code** | [www.88code.ai](https://www.88code.ai) | [是](https://docs.88code.org/ClaudeCode/Windows.html) | [是](https://docs.88code.org/Codex/Windows.html) | - | [价格](https://docs.88code.org/88code/pricing.html) | 开放 | 以包月套餐为主（按日额度），另有按量包；文档写每账号最多 4 个客户端并发；88code.org 跳转到 88code.ai | 2026-10-29 |
| **AIHubMix** | [aihubmix.com](https://aihubmix.com) | [是](https://docs.aihubmix.com/en/api/Claude-Code) | [是](https://docs.aihubmix.com/cn/api/Codex-CLI) | 信用卡 | [价格](https://aihubmix.com/models) | 开放 | 充值仅 Stripe，单次最低 $15；备用域名 api.inferera.com；Codex 需 wire_api=responses | 2026-10-29 |
| **AnyRouter** | [anyrouter.top](https://anyrouter.top) | [是](https://docs.anyrouter.top/) | 否 | - | - | 未核实 | 公益站，官方文档称注册赠送额度、不需付款；注册页有人机验证，官网首页无法抓取文本 | 2026-10-29 |
| **APIMart** | [apimart.ai](https://apimart.ai) | [是](https://docs.apimart.ai/en/integrations/dev-tool/claude-code.md) | [是](https://docs.apimart.ai/en/integrations/dev-tool/codex-cli.md) | 信用卡、支付宝、PayPal、加密货币 | [价格](https://apimart.ai/pricing) | 开放 | 按量付费，会员等级有不同折扣；Claude 思考变体加 -thinking 后缀；Codex 需 wire_api=responses | 2026-10-29 |
| **APINebula** | [apinebula.ai](https://apinebula.ai) | [是](https://docs.apinebula.com/docs/cli/claude-code) | [是](https://docs.apinebula.com/docs/cli/codex) | - | [价格](https://apinebula.ai/zh/pricing) | 开放 | Claude Code 需选「Claude Code全球高防」令牌分组且模型列表留空，否则 403；Codex 用 CODEX 分组；官网为纯前端渲染，支付方式未在官方页面读到 | 2026-10-29 |
| **CloseAI** | [www.closeai-asia.com](https://www.closeai-asia.com) | [是](https://doc.closeai-asia.com/tutorial/integrations/claude-code.html) | [是](https://doc.closeai-asia.com/tutorial/integrations/codex-cli.html) | 支付宝、微信、信用卡、对公转账 | [价格](https://www.closeai-asia.com/pricing) | 开放 | 价格为官方价乘倍率（文档列 1.1x 到 1.5x 三档）；Anthropic 协议走 /anthropic 前缀，OpenAI 兼容走 /v1 | 2026-10-29 |
| **CoderPlan** | [coderplan.ai](https://coderplan.ai) | [是](https://coderplan.ai/docs/setup/claude-code) | [是](https://coderplan.ai/docs/setup/codex-cli) | 信用卡 | [价格](https://coderplan.ai/pricing) | 开放 | 按量付费，充值走 Stripe，文档称暂不支持国内发票；Codex 需 wire_api=responses | 2026-10-29 |
| **DuckCoding** | [www.duckcoding.ai](https://www.duckcoding.ai) | [是](https://docs.duckcoding.ai/) | [是](https://docs.duckcoding.ai/) | - | [价格](https://www.duckcoding.ai/pricing) | 开放 | 官网与文档在 .ai 域名，duckcoding.com 2026-10-29 显示域名未绑定；需分别创建 Claude Code 专用和 Codex 专用分组令牌；按量计费，各分组另乘倍率 | 2026-10-29 |
| **laozhang.ai** | [www.laozhang.ai](https://www.laozhang.ai) | [是](https://docs.laozhang.ai/en/scenarios/programming/claude-code) | [是](https://docs.laozhang.ai/scenarios/programming/codex-cli.md) | 信用卡、对公转账 | [价格](https://docs.laozhang.ai/pricing.md) | 开放 | 注册仅支持 Gmail，文档称服务可用性以企业白名单审核为准；Claude 单次输出上限 32768 | 2026-10-29 |
| **OhMyGPT** | [www.ohmygpt.com](https://www.ohmygpt.com) | [是](https://docs.ohmygpt.com/docs/code-cli) | [是](https://docs.ohmygpt.com/docs/code-cli) | 支付宝、微信、PayPal、信用卡 | [价格](https://www.ohmygpt.com/models) | 开放 | 官方推荐 npx omgvibe 一键写入 Claude Code / Codex 配置；另有 CDN 镜像域名 apic1.ohmycdn.com；首页公告 2026-10-15 称 Codex 折扣渠道已停用 | 2026-10-29 |
| **OpenRouter** | [openrouter.ai](https://openrouter.ai) | [是](https://openrouter.ai/docs/guides/guides/claude-code-integration) | [是](https://openrouter.ai/docs/cookbook/coding-agents/codex-cli) | 信用卡、支付宝、USDC | [价格](https://openrouter.ai/pricing) | 开放 | 模型 ID 带厂商前缀（anthropic/…）；购买额度收平台费（Standard 5.5%）；Codex 需 wire_api=responses | 2026-10-29 |
| **PackyAPI（原 PackyCode）** | [www.packyapi.com](https://www.packyapi.com) | [是](https://docs.packyapi.com/docs/cli/2-claude.html) | [是](https://docs.packyapi.com/docs/cli/3-codex.html) | 支付宝、微信 | [价格](https://www.packyapi.ai/pricing) | 开放 | Claude Code 和 Codex 要分别用 CC 分组和 Codex 分组的令牌；文档另给优化线路 slb-v1.api.fan；官网 packyapi.com 与 packyapi.ai 并存 | 2026-10-29 |
| **QCode** | [qcode.cc](https://qcode.cc) | [是](https://docs.qcode.cc/docs/getting-started/installation) | [是](https://docs.qcode.cc/docs/ide/codex) | 支付宝、微信、信用卡、Apple Pay、加密货币 | [价格](https://qcode.cc/pricing) | 开放 | 个人套餐按日额度包月，另有 7 天有效的按量包；大陆推荐 asia.qcode.cc 入口；Claude 模型只走 Anthropic 接口 | 2026-10-29 |
| **TeamoRouter**（本仓库维护者） | [teamorouter.com](https://teamorouter.com) | [是](https://teamorouter.com/zh/docs/install-claude-code) | [是](https://teamorouter.com/zh/docs/install-codex) | 支付宝、信用卡、USDT | [价格](https://teamorouter.com/zh/pricing) | 开放 | 按量计费；同一个 Key 同时走 Anthropic 兼容和 OpenAI 兼容端点；本仓库维护者 | 2026-10-29 |
| **YesCode** | [co.yes.vg](https://co.yes.vg) | 否 | 否 | - | - | 未核实 | 官网为纯前端应用，文档和价格页需站内渲染；Base URL 取自官方脚本 setup-claude-code.sh 和 setup-codex.sh（Codex 用 wire_api=responses） | 2026-10-29 |
| **云雾AI** | [yunwu.ai](https://yunwu.ai) | [是](https://s.apifox.cn/apidoc/docs-site/5427167/doc-7010249) | [是](https://s.apifox.cn/apidoc/docs-site/5427167/doc-7422014) | - | - | 开放 | 令牌须选 Claude Code 专属分组，default 与逆向分组不支持工具调用；Codex 需 wire_api=responses；价格在控制台内，公开页面未列支付方式 | 2026-10-29 |
| **灵眸AI** | [api.lmuai.ai](https://api.lmuai.ai) | [是](https://docs.lmuai.ai/docs/tools/claude-code) | [是](https://docs.lmuai.ai/docs/tools/codex-cli-mac) | - | [价格](https://api.lmuai.ai/pricing) | 开放 | 月卡按平台分 Claude 和 GPT 两类，也支持余额按量；一个 Key 对应一个分组，跨组会 400；文档称挂代理可能断流 | 2026-10-29 |
| **灵芽 API** | [api.lingyaai.cn](https://api.lingyaai.cn) | [是](https://api.lingyaai.cn/aicoding.html#claude) | [是](https://api.lingyaai.cn/aicoding.html#codex) | - | [价格](https://api.lingyaai.cn/modellist/) | 开放 | Claude Code / Codex / Gemini CLI 各有专用分组；官方 Claude Code 示例配置的是 glm-5.2 等国产模型，FAQ 模型列表未出现 Claude 模型 ID | 2026-10-29 |
| **神马中转API** | [api.whatai.cc](https://api.whatai.cc) | [是](https://docs.whatai.cc/docs/otherai/devtools/claudecode/) | [是](https://docs.whatai.cc/docs/otherai/devtools/codex/) | 支付宝、微信、USDT | - | 已停止 | 2026-10-29 官网首页为「关闭及退款说明」，服务已关闭；文档站仍在线。保留条目供参考，不再探测 | 2026-10-29 |
<!-- DIRECTORY:END -->

表按名称排序，不是排名。「Claude Code / Codex CLI」列里的「是」链接到该家自己的接入文档；「否」表示我们在官网没找到对应文档，不代表不能用。支付方式只写官网明确列出的。想补充或更正，见 [CONTRIBUTING.md](CONTRIBUTING.md)。

## 可用性探测

<!-- MONITOR:START -->
最近 7 天 · 更新于 2026-10-29 02:03 UTC · 探测节点：GitHub Actions（美国）· 每 6 小时一轮

| 服务商 | 端点 | 样本数 | 网关应答率 | 端点有效率 | TTFB P50 | TTFB P95 | 认证请求成功率 |
|---|---|---|---|---|---|---|---|
| 302.AI | `/v1/messages` | 2 | 100.0% | 100.0% | 566 ms | 2737 ms | - |
| 302.AI | `/v1/chat/completions` | 2 | 100.0% | 100.0% | 565 ms | 1778 ms | - |
| 88code | `/v1/messages` | 2 | 100.0% | 100.0% | 451 ms | 705 ms | - |
| 88code | `/v1/chat/completions` | 2 | 100.0% | 100.0% | 212 ms | 613 ms | - |
| AIHubMix | `/v1/messages` | 2 | 100.0% | 100.0% | 130 ms | 159 ms | - |
| AIHubMix | `/v1/chat/completions` | 2 | 100.0% | 100.0% | 116 ms | 129 ms | - |
| AnyRouter | `/v1/messages` | 2 | 100.0% | 100.0% | 1312 ms | 1565 ms | - |
| APIMart | `/v1/messages` | 2 | 100.0% | 100.0% | 230 ms | 352 ms | - |
| APIMart | `/v1/chat/completions` | 2 | 100.0% | 100.0% | 199 ms | 295 ms | - |
| APINebula | `/v1/messages` | 2 | 100.0% | 100.0% | 106 ms | 215 ms | - |
| APINebula | `/v1/chat/completions` | 2 | 100.0% | 100.0% | 96 ms | 300 ms | - |
| CloseAI | `/v1/messages` | 2 | 100.0% | 100.0% | 113 ms | 264 ms | - |
| CloseAI | `/v1/chat/completions` | 2 | 100.0% | 100.0% | 116 ms | 133 ms | - |
| CoderPlan | `/v1/messages` | 2 | 100.0% | 100.0% | 630 ms | 712 ms | - |
| CoderPlan | `/v1/chat/completions` | 2 | 100.0% | 100.0% | 608 ms | 672 ms | - |
| DuckCoding | `/v1/messages` | 2 | 100.0% | 100.0% | 320 ms | 1151 ms | - |
| DuckCoding | `/v1/chat/completions` | 2 | 100.0% | 100.0% | 122 ms | 263 ms | - |
| laozhang.ai | `/v1/messages` | 2 | 100.0% | 100.0% | 87 ms | 340 ms | - |
| laozhang.ai | `/v1/chat/completions` | 2 | 100.0% | 100.0% | 83 ms | 217 ms | - |
| OhMyGPT | `/v1/messages` | 2 | 100.0% | 100.0% | 130 ms | 208 ms | - |
| OhMyGPT | `/v1/chat/completions` | 2 | 100.0% | 100.0% | 61 ms | 178 ms | - |
| OpenRouter | `/v1/messages` | 2 | 100.0% | 100.0% | 57 ms | 158 ms | - |
| OpenRouter | `/v1/chat/completions` | 2 | 100.0% | 100.0% | 41 ms | 74 ms | - |
| PackyAPI（原 PackyCode） | `/v1/messages` | 2 | 100.0% | 100.0% | 237 ms | 481 ms | - |
| PackyAPI（原 PackyCode） | `/v1/chat/completions` | 2 | 100.0% | 100.0% | 51 ms | 164 ms | - |
| QCode | `/v1/messages` | 2 | 100.0% | 100.0% | 242 ms | 388 ms | - |
| QCode | `/v1/chat/completions` | 2 | 100.0% | 100.0% | 231 ms | 383 ms | - |
| TeamoRouter | `/v1/messages` | 2 | 100.0% | 100.0% | 1302 ms | 2700 ms | 100.0% (2) |
| TeamoRouter | `/v1/chat/completions` | 2 | 100.0% | 100.0% | 817 ms | 1228 ms | 100.0% (2) |
| YesCode | `/v1/messages` | 2 | 100.0% | 100.0% | 510 ms | 617 ms | - |
| YesCode | `/v1/chat/completions` | 2 | 100.0% | 100.0% | 449 ms | 504 ms | - |
| 云雾AI | `/v1/messages` | 2 | 100.0% | 100.0% | 465 ms | 484 ms | - |
| 云雾AI | `/v1/chat/completions` | 2 | 100.0% | 100.0% | 469 ms | 491 ms | - |
| 灵眸AI | `/v1/messages` | 2 | 100.0% | 100.0% | 722 ms | 802 ms | - |
| 灵眸AI | `/v1/chat/completions` | 2 | 100.0% | 100.0% | 529 ms | 636 ms | - |
| 灵芽 API | `/v1/messages` | 2 | 100.0% | 100.0% | 701 ms | 951 ms | - |
| 灵芽 API | `/v1/chat/completions` | 2 | 100.0% | 100.0% | 919 ms | 1210 ms | - |
| 神马中转API | `/v1/messages` | 0 | - | - | - | - | - |
| 神马中转API | `/v1/chat/completions` | 0 | - | - | - | - | - |
<!-- MONITOR:END -->

<details>
<summary>最近 30 天</summary>

<!-- MONITOR30:START -->
最近 30 天

| 服务商 | 端点 | 样本数 | 网关应答率 | 端点有效率 | TTFB P50 | TTFB P95 | 认证请求成功率 |
|---|---|---|---|---|---|---|---|
| 302.AI | `/v1/messages` | 2 | 100.0% | 100.0% | 566 ms | 2737 ms | - |
| 302.AI | `/v1/chat/completions` | 2 | 100.0% | 100.0% | 565 ms | 1778 ms | - |
| 88code | `/v1/messages` | 2 | 100.0% | 100.0% | 451 ms | 705 ms | - |
| 88code | `/v1/chat/completions` | 2 | 100.0% | 100.0% | 212 ms | 613 ms | - |
| AIHubMix | `/v1/messages` | 2 | 100.0% | 100.0% | 130 ms | 159 ms | - |
| AIHubMix | `/v1/chat/completions` | 2 | 100.0% | 100.0% | 116 ms | 129 ms | - |
| AnyRouter | `/v1/messages` | 2 | 100.0% | 100.0% | 1312 ms | 1565 ms | - |
| APIMart | `/v1/messages` | 2 | 100.0% | 100.0% | 230 ms | 352 ms | - |
| APIMart | `/v1/chat/completions` | 2 | 100.0% | 100.0% | 199 ms | 295 ms | - |
| APINebula | `/v1/messages` | 2 | 100.0% | 100.0% | 106 ms | 215 ms | - |
| APINebula | `/v1/chat/completions` | 2 | 100.0% | 100.0% | 96 ms | 300 ms | - |
| CloseAI | `/v1/messages` | 2 | 100.0% | 100.0% | 113 ms | 264 ms | - |
| CloseAI | `/v1/chat/completions` | 2 | 100.0% | 100.0% | 116 ms | 133 ms | - |
| CoderPlan | `/v1/messages` | 2 | 100.0% | 100.0% | 630 ms | 712 ms | - |
| CoderPlan | `/v1/chat/completions` | 2 | 100.0% | 100.0% | 608 ms | 672 ms | - |
| DuckCoding | `/v1/messages` | 2 | 100.0% | 100.0% | 320 ms | 1151 ms | - |
| DuckCoding | `/v1/chat/completions` | 2 | 100.0% | 100.0% | 122 ms | 263 ms | - |
| laozhang.ai | `/v1/messages` | 2 | 100.0% | 100.0% | 87 ms | 340 ms | - |
| laozhang.ai | `/v1/chat/completions` | 2 | 100.0% | 100.0% | 83 ms | 217 ms | - |
| OhMyGPT | `/v1/messages` | 2 | 100.0% | 100.0% | 130 ms | 208 ms | - |
| OhMyGPT | `/v1/chat/completions` | 2 | 100.0% | 100.0% | 61 ms | 178 ms | - |
| OpenRouter | `/v1/messages` | 2 | 100.0% | 100.0% | 57 ms | 158 ms | - |
| OpenRouter | `/v1/chat/completions` | 2 | 100.0% | 100.0% | 41 ms | 74 ms | - |
| PackyAPI（原 PackyCode） | `/v1/messages` | 2 | 100.0% | 100.0% | 237 ms | 481 ms | - |
| PackyAPI（原 PackyCode） | `/v1/chat/completions` | 2 | 100.0% | 100.0% | 51 ms | 164 ms | - |
| QCode | `/v1/messages` | 2 | 100.0% | 100.0% | 242 ms | 388 ms | - |
| QCode | `/v1/chat/completions` | 2 | 100.0% | 100.0% | 231 ms | 383 ms | - |
| TeamoRouter | `/v1/messages` | 2 | 100.0% | 100.0% | 1302 ms | 2700 ms | 100.0% (2) |
| TeamoRouter | `/v1/chat/completions` | 2 | 100.0% | 100.0% | 817 ms | 1228 ms | 100.0% (2) |
| YesCode | `/v1/messages` | 2 | 100.0% | 100.0% | 510 ms | 617 ms | - |
| YesCode | `/v1/chat/completions` | 2 | 100.0% | 100.0% | 449 ms | 504 ms | - |
| 云雾AI | `/v1/messages` | 2 | 100.0% | 100.0% | 465 ms | 484 ms | - |
| 云雾AI | `/v1/chat/completions` | 2 | 100.0% | 100.0% | 469 ms | 491 ms | - |
| 灵眸AI | `/v1/messages` | 2 | 100.0% | 100.0% | 722 ms | 802 ms | - |
| 灵眸AI | `/v1/chat/completions` | 2 | 100.0% | 100.0% | 529 ms | 636 ms | - |
| 灵芽 API | `/v1/messages` | 2 | 100.0% | 100.0% | 701 ms | 951 ms | - |
| 灵芽 API | `/v1/chat/completions` | 2 | 100.0% | 100.0% | 919 ms | 1210 ms | - |
| 神马中转API | `/v1/messages` | 0 | - | - | - | - | - |
| 神马中转API | `/v1/chat/completions` | 0 | - | - | - | - | - |
<!-- MONITOR30:END -->

</details>

### 监控方法

- 脚本：[`scripts/probe.py`](scripts/probe.py)，原始数据：[`data/probes/`](data/probes/)，每行一条 JSON。
- **无 Key 探测**（所有家）：向 `anthropic_base/v1/messages` 和 `openai_base/v1/chat/completions` 各发一个带假 Key 的最小请求。
  - **网关应答率**：curl 拿到任何 5xx 以下的 HTTP 响应，说明网关在线。
  - **端点有效率**：响应是 400 / 401 / 403 / 422 / 429 之一，说明端点存在并且校验了请求。404 或 405 算网关在线但端点路径不对。
  - **TTFB**：从发起请求到收到第一个字节的时间，取网关有应答的样本算 P50 / P95。
- **认证探测**（只有维护者自己有 Key 的 TeamoRouter）：真实请求 `max_tokens=8`，200 且回包里有 "ok" 算成功。这一列其他家是 `-`，不是失败。
- 节点在 GitHub Actions 的美国机房，**反映的是海外到各家网关的可达性和延迟，不等于国内体验**。想要国内节点的数据，可以在自己机器上跑同一脚本（`PROBE_VANTAGE=cn-xxx python3 scripts/probe.py`）并提 PR。
- 一轮一个样本，每 6 小时一轮，一天 4 个样本。样本少的时候百分比波动大，看 30 天的表更稳。

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
