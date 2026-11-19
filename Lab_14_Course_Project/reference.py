"""Lab 14: integrated Campus Help-Desk Agent reference implementation."""
from source_code.campus_helpdesk import Memory, node_graph_run

if __name__ == "__main__":
    memory, audit, prompts = Memory(), [], []
    result = node_graph_run(
        "student",
        "How do I connect to wifi on campus?",
        memory,
        audit,
        prompts,
    )
    print(result)
    print({"prompt_log": prompts, "audit_log": audit, "memory": memory.history})
