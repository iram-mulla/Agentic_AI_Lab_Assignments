import csv, io

DATA = """event,signups,category
AI Talk,12,technical
Hackathon,9,technical
Career Panel,11,social
"""

rows = list(csv.DictReader(io.StringIO(DATA)))
technical = [r for r in rows if r["category"] == "technical"]
trace = [
    {"step": "read_csv", "output": rows},
    {"step": "filter_category", "input": "technical", "output": technical},
]
if not technical:
    raise RuntimeError("filter produced an empty result")
average = sum(int(r["signups"]) for r in technical) / len(technical)
trace.append({"step": "calculator", "operation": "average", "output": average})
print({"average": average, "trace": trace})
