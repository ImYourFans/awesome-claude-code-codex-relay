# 贡献指南 / Contributing

## 收录一家服务商 / Add a provider

1. 在 `providers.json` 末尾加一个对象，字段见已有条目。`website`、`anthropic_base` 或 `openai_base` 至少一个、`sources` 必填。
2. 每个字段都要能在 `sources` 里的公开页面上找到。价格、支付方式、支持的客户端只写官网或文档明确写了的。
3. `notes` 只写事实（比如「仅支持 Claude Code 客户端的分组」「按套餐订阅」），不写评价（「稳定」「靠谱」「便宜」都不收）。
4. 如果你代表该服务商，在 PR 里说明。这不影响收录，但会写进 PR 记录。
5. 运行 `python3 scripts/build_readme.py` 重新生成 README 表格，把生成结果一起提交。
6. 不接受返利链接、邀请码。`website` 必须是干净的官网 URL。

Add one object to `providers.json` (see existing entries). Every value must be verifiable on a page listed in `sources`. Facts only in `notes`, no adjectives. Disclose if you represent the provider. No affiliate links or invite codes. Run `python3 scripts/build_readme.py` and commit the regenerated tables.

## 更正 / Corrections

直接提 PR 或 issue，附上能看到正确信息的 URL。服务商停止注册或停服，把 `registration` 改成 `closed` 并在 `notes` 写公告日期。

## 监控数据 / Probe data

`data/probes/*.jsonl` 由 GitHub Actions 自动写入，不要手改。探测方法见 README「监控方法」一节。如果你在其他地区跑了同一脚本（`PROBE_VANTAGE=<地区>` 并设置 `PROBE_TIMEOUT`），欢迎把结果文件以 PR 提交到 `data/probes/vantage-<地区>/`。
