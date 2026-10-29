#!/usr/bin/env bash
# 国内探测节点：放在一台能直连公网、不走代理的中国大陆机器上，crontab 每 6 小时跑一次，例如
#   23 */6 * * * /path/to/repo/scripts/cron-cn.sh >> /var/log/relay-probe-cn.log 2>&1
# 需要：git 能推本仓库（deploy key 或 token）、python3、curl。KEY_TEAMOROUTER 可不设，不设就没有认证探测。
set -euo pipefail
cd "$(dirname "$0")/.."
git pull -q --rebase origin main
PROBE_VANTAGE=cn-mainland PROBE_FILE=latest-cn python3 scripts/probe.py
python3 scripts/build_readme.py
git add data README.md README.en.md
git diff --cached --quiet && exit 0
git -c user.name="relay-probe-cn[bot]" -c user.email="relay-probe-cn@users.noreply.github.com" \
    commit -q -m "probe(cn): $(date -u +%Y-%m-%dT%H:%MZ) [skip ci]"
git pull -q --rebase origin main
git push -q origin main
