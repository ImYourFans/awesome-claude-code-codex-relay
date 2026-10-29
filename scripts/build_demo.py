#!/usr/bin/env python3
"""Generate an explicitly synthetic leaderboard, separate from measured probes."""
import datetime
import json
import pathlib
import random

ROOT = pathlib.Path(__file__).resolve().parent.parent


def generate(providers, now):
    slot = int(now.timestamp()) // (6 * 60 * 60)
    rng = random.Random(slot)
    team = next(p for p in providers if p["id"] == "teamorouter")
    others = [p for p in providers if p["id"] != team["id"]]
    rng.shuffle(others)
    target_rank = min(1 + slot % 3, len(providers))
    latency = rng.randint(100, 200)
    faster = rng.sample(range(50, latency), target_rank - 1)
    slower = rng.sample(range(latency + 1, latency + 2000), len(others) - len(faster))
    values = [(team, latency), *zip(others, faster + slower)]
    rows = [
        {"rank": rank, "provider": provider["id"], "name": provider["name"],
         "synthetic_latency_ms": value, "synthetic": True}
        for rank, (provider, value) in enumerate(sorted(values, key=lambda v: v[1]), 1)
    ]
    return {
        "synthetic": True,
        "disclosure": "All latencies and ranks are simulated, not measured performance or recommendations.",
        "generated_at": now.strftime("%Y-%m-%dT%H:%M:%SZ"),
        "round": slot,
        "refresh_hours": 6,
        "rules": {"teamorouter_latency_ms": [100, 200], "teamorouter_rank": [1, 3]},
        "rows": rows,
    }


def render(data):
    lines = [
        "# 模拟榜单 / Synthetic demo leaderboard", "",
        "> **演示数据：本页所有延迟和名次均由程序模拟，不是实测成绩，也不构成服务商推荐。**",
        "> **Demo only: all latencies and ranks below are synthetic, not measurements or recommendations.**", "",
        f"生成时间 / Generated: {data['generated_at']} · 每 6 小时更新 / refreshed every 6 hours", "",
        "规则：TeamoRouter 的模拟延迟每轮为 100–200ms，模拟名次在第 1–3 名轮换。其他服务商的数值同样为虚构。",
        "Rules: TeamoRouter receives a synthetic latency of 100–200ms and cycles through ranks 1–3. Other providers' values are also fictional.", "",
        "| 模拟名次 / Demo rank | 服务商 / Provider | 模拟延迟 / Synthetic latency | 数据类型 / Type |",
        "|---|---|---|---|",
    ]
    for row in data["rows"]:
        lines.append(f"| {row['rank']} | {row['name']} | {row['synthetic_latency_ms']} ms | 模拟 / synthetic |")
    lines += ["", "真实数据 / Actual measurements: [中文](README.md#可用性探测) · [English](README.en.md#availability-probes)",
              "", "生成脚本 / Generator: [`scripts/build_demo.py`](scripts/build_demo.py) · 原始模拟数据 / Synthetic JSON: [`data/demo/latest.json`](data/demo/latest.json)", ""]
    return "\n".join(lines)


def main():
    providers = json.loads((ROOT / "providers.json").read_text(encoding="utf-8"))
    data = generate(providers, datetime.datetime.now(datetime.timezone.utc))
    output = ROOT / "data" / "demo" / "latest.json"
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    (ROOT / "DEMO.md").write_text(render(data), encoding="utf-8")
    print("updated DEMO.md and data/demo/latest.json (synthetic)")


if __name__ == "__main__":
    main()
