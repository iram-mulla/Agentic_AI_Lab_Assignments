"""Mini OpenCLA-style runtime."""
from datetime import datetime

def tool_word_count(text):
    return {"count": len(text.split())}

def tool_lookup_contact(name, contacts):
    return contacts.get(name, {"error": f"no contact found for {name}"})

TOOLS = {"word_count": tool_word_count, "lookup_contact": tool_lookup_contact}

class Memory:
    def __init__(self):
        self.store = {}

    def scope(self, user):
        return self.store.setdefault(user, {})

class Audit:
    def __init__(self):
        self.entries = []

    def log(self, task, skill_name, tool_calls, result=None, error=None):
        self.entries.append({
            "timestamp": datetime.now().isoformat(timespec="seconds"),
            "task": task,
            "skill": skill_name,
            "tool_calls": tool_calls,
            "result": result,
            "error": error,
        })

class SummarizeNotesSkill:
    def __init__(self, memory_scope):
        self.memory_scope = memory_scope
        self.tool_calls = []

    def execute(self, task):
        result = TOOLS["word_count"](task["text"])
        self.tool_calls.append({"tool": "word_count", "output": result})
        self.memory_scope["last_note_length"] = result["count"]
        return f"Summary stub: note has {result['count']} words."

class DraftEmailSkill:
    CONTACTS = {"Dr. Meena": {"email": "meena@example.edu"}}

    def __init__(self, memory_scope):
        self.memory_scope = memory_scope
        self.tool_calls = []

    def execute(self, task):
        contact = TOOLS["lookup_contact"](task["to"], self.CONTACTS)
        self.tool_calls.append({"tool": "lookup_contact", "output": contact})
        if "error" in contact:
            raise RuntimeError(contact["error"])
        return f"Draft email to {contact['email']}: '{task['subject']}'"

SKILL_REGISTRY = {"summarize_notes": SummarizeNotesSkill, "draft_email": DraftEmailSkill}

def receive_task(task, user, memory, audit):
    skill_name = task["skill"]
    skill_class = SKILL_REGISTRY[skill_name]
    skill = skill_class(memory.scope(user))
    try:
        result = skill.execute(task)
        audit.log(task, skill_name, skill.tool_calls, result=result)
        return result
    except Exception as exc:
        audit.log(task, skill_name, skill.tool_calls, error=str(exc))
        raise

if __name__ == "__main__":
    memory, audit = Memory(), Audit()
    print(receive_task({"skill": "summarize_notes", "text": "Agentic AI systems combine goals tools skills memory"}, "uday", memory, audit))
    print(receive_task({"skill": "draft_email", "to": "Dr. Meena", "subject": "Lab guide review"}, "uday", memory, audit))
    try:
        receive_task({"skill": "draft_email", "to": "Unknown Person", "subject": "Hello"}, "uday", memory, audit)
    except RuntimeError as exc:
        print(exc)
