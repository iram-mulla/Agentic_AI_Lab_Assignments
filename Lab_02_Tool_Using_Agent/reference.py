"""Campus Data Assistant with structured tool contracts."""
import csv
import io

SIGNUPS_CSV = """event,signups
AI Club Talk,12
Hackathon Kickoff,9
Robotics Demo,15
GenAI Workshop,7
Capstone Expo,20
Career Panel,11
"""
EVENTS = {"Hackathon Kickoff": {"date": "2026-07-05", "location": "Innovation Lab"}}

def calculator(operation, values):
    if operation == "sum":
        return {"result": sum(values)}
    if operation == "average":
        return {"result": sum(values) / len(values)} if values else {"error": "no values supplied"}
    return {"error": f"unsupported operation: {operation}"}

def read_csv(source_text=SIGNUPS_CSV):
    rows = list(csv.DictReader(io.StringIO(source_text)))
    return {"rows": rows, "row_count": len(rows)} if rows else {"error": "empty file", "rows": [], "row_count": 0}

def mock_events_api(event_name):
    if event_name not in EVENTS:
        return {"error": f"no event metadata found for '{event_name}'"}
    return EVENTS[event_name]

TOOLS = {"calculator": calculator, "read_csv": read_csv, "events_api": mock_events_api}

class CampusDataAssistant:
    def __init__(self):
        self.trace = []

    def _call(self, tool_name, reason, **kwargs):
        result = TOOLS[tool_name](**kwargs)
        self.trace.append({"tool": tool_name, "reason": reason, "input": kwargs, "output": result})
        if "error" in result:
            raise RuntimeError(f"{tool_name} failed: {result['error']}")
        return result

    def answer(self, question):
        lower = question.lower()
        if "average" in lower and "sign" in lower:
            csv_result = self._call("read_csv", "sign-up counts are in the CSV")
            values = [int(row["signups"]) for row in csv_result["rows"]]
            total = self._call("calculator", "sum the signup values", operation="sum", values=values)
            average = self._call("calculator", "compute the event average", operation="average", values=values)
            return f"Total sign-ups: {total['result']}. Average per event: {average['result']:.2f}."
        if "where" in lower and "hackathon" in lower:
            record = self._call("events_api", "location metadata is in the events API", event_name="Hackathon Kickoff")
            return f"Hackathon Kickoff is at {record['location']} on {record['date']}."
        if "where" in lower and "capstone" in lower:
            try:
                record = self._call("events_api", "check events API metadata", event_name="Capstone Expo")
                return f"Capstone Expo is at {record['location']} on {record['date']}."
            except RuntimeError:
                return "I don't have location/date metadata for Capstone Expo."
        return "I don't have a tool path configured for that question."

if __name__ == "__main__":
    assistant = CampusDataAssistant()
    print(assistant.answer("How many students signed up and what's the average per event?"))
    print(assistant.answer("Where and when is the Hackathon Kickoff?"))
    print(assistant.answer("Where and when is the Capstone Expo?"))
