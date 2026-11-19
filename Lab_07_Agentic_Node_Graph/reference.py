"""Lab 7: campus app agentic node graph."""

class Node:
    def __init__(self, name, owner, action, success_fn, on_fail):
        self.name = name
        self.owner = owner
        self.action = action
        self.success_fn = success_fn
        self.on_fail = on_fail

def requirements(state):
    state["requirements"] = ["user login", "event listing", "RSVP button"]
    return state

def planning(state):
    state["tasks"] = {item: f"task_for({item})" for item in state["requirements"]}
    return state

def building(state):
    state["build_ok"] = not state.get("force_build_fail", False)
    if state["build_ok"]:
        state["code"] = "app.py generated"
    return state

def testing(state):
    state["tests_passed"] = state["build_ok"]
    return state

def review(state):
    state["review_clean"] = state["tests_passed"]
    return state

def human_gate(state):
    state["human_signoff"] = state["review_clean"]
    return state

GRAPH = [
    Node("requirement", "requirement_agent", requirements, lambda s: len(s.get("requirements", [])) >= 3, "escalate"),
    Node("planner", "planner_agent", planning, lambda s: len(s.get("tasks", {})) == len(s["requirements"]), "return_to_requirement"),
    Node("builder", "builder_agent", building, lambda s: s.get("build_ok", False), "retry_build_or_escalate"),
    Node("tester", "tester_agent", testing, lambda s: s.get("tests_passed", False), "route_back_to_builder"),
    Node("reviewer", "reviewer_agent", review, lambda s: s.get("review_clean", False), "route_back_to_builder"),
    Node("human_gate", "human", human_gate, lambda s: s.get("human_signoff", False), "return_to_planner"),
]

def simulate(force_build_fail=False):
    state = {"force_build_fail": force_build_fail}
    trace = []
    for node in GRAPH:
        state = node.action(state)
        success = node.success_fn(state)
        trace.append({"node": node.name, "owner": node.owner, "success": success})
        if not success:
            trace.append({"node": node.name, "failure_behavior_triggered": node.on_fail})
            break
    return trace

if __name__ == "__main__":
    print("success:", simulate(False))
    print("builder failure:", simulate(True))
