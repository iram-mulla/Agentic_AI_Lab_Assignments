import sys
sys.path.insert(0, ".")
from Lab_07_Agentic_Node_Graph.reference import simulate

GRAPH_ADDITION = {"node": "security_scan", "owner": "security_agent", "input": "built artifact", "output": "scan result", "success": "no critical findings", "failure": "reject release"}

def simulate_security(scan_fails=False):
    trace = [
        {"node": "requirement", "success": True},
        {"node": "builder", "success": True},
        {"node": "security_scan", "success": not scan_fails, "finding": "critical vulnerability" if scan_fails else "clean"},
    ]
    if scan_fails: trace.append({"failure_behavior": "reject release"})
    else: trace.append({"node": "tester", "success": True})
    return trace

print(GRAPH_ADDITION)
print(simulate_security(False))
print(simulate_security(True))
