from datetime import date, timedelta

records = [
    {"topic": "database", "fact": "PostgreSQL", "date": date.today()},
    {"topic": "database", "fact": "MySQL", "date": date.today() - timedelta(days=90)},
]

retention_days = 30
for record in records:
    age = (date.today() - record["date"]).days
    warning = f"this decision is from {age} days ago and may be out of date" if age > retention_days else "fresh"
    print(record["fact"], warning)
