class SummarizeSkill:
    def __init__(self, memory):
        self.memory = memory
        self.tool_calls = []

    def execute(self, task):
        count = len(task["text"].split())
        self.memory["last_note_length"] = count
        return f"Summary: {count} words"


task_counts = {}
audit = []
LIMIT = 3

def receive_task(task, user):
    task_counts[user] = task_counts.get(user, 0)
    if task_counts[user] >= LIMIT:
        audit.append({"user": user, "skill": task["skill"], "error": "rate limit exceeded"})
        return {"rejected": True, "reason": "at most 3 tasks per session"}

    task_counts[user] += 1
    memory = {}
    result = SummarizeSkill(memory).execute(task)
    audit.append({"user": user, "skill": task["skill"], "tool_calls": [], "result": result, "error": None})
    return result

for attempt in range(1, 5):
    print(f"attempt_{attempt}", receive_task({"skill": "summarize", "text": "short note"}, "uday"))
