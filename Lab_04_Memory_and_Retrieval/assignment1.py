memory = {
    "database": [{"fact": "chose PostgreSQL", "date": "2026-07-03"}],
    "hosting": [{"fact": "selected Azure", "date": "2026-07-05"}],
}

for topic in ("database", "hosting"):
    print(topic, memory[topic])
assert "Azure" not in str([r["fact"] for r in memory["database"]])
