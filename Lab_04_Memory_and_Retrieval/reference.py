"""Tagged project memory with scoped retrieval and permission-gated writes."""
from dataclasses import dataclass
from datetime import date

@dataclass
class MemoryRecord:
    topic: str
    fact: str
    date: str
    source: str = "memory"

class ProjectMemory:
    def __init__(self):
        self.records = []
        self.allowed_writers = {"team_lead"}

    def retrieve(self, topic):
        return [record for record in self.records if record.topic == topic]

    def write(self, record, user_role):
        if user_role not in self.allowed_writers:
            raise PermissionError(f"role '{user_role}' is not permitted to write memory")
        self.records.append(record)

class ProjectAssistant:
    def __init__(self, memory):
        self.memory = memory
        self.session_facts = {}

    def answer(self, topic):
        hits = self.memory.retrieve(topic)
        if not hits:
            return f"[session] No stored decision on '{topic}'."
        latest = hits[-1]
        return f"[memory, dated {latest.date}] {latest.fact}"

    def receive_statement(self, topic, new_fact, user_role):
        hits = self.memory.retrieve(topic)
        if hits and hits[-1].fact.lower() != new_fact.lower():
            return {"conflict": True, "message": f"This conflicts with stored decision '{hits[-1].fact}'. Should I update memory?"}
        self.memory.write(MemoryRecord(topic, new_fact, str(date.today())), user_role)
        return {"conflict": False, "written": True}

if __name__ == "__main__":
    memory = ProjectMemory()
    memory.write(MemoryRecord("database", "we chose PostgreSQL", "2026-07-03"), "team_lead")
    assistant = ProjectAssistant(memory)
    print(assistant.answer("database"))
    print(assistant.receive_statement("database", "we're switching to SQLite", "member"))
