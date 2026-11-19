"""Focused assertions for rubric-sensitive assignment scenarios."""
import io
import json
import sys
from contextlib import redirect_stdout
from pathlib import Path

root = Path(__file__).resolve().parent

def load_module(relative_path):
    sys.path.insert(0, str(root / relative_path.parent))
    module_name = relative_path.stem
    if module_name in sys.modules:
        del sys.modules[module_name]
    namespace = {}
    exec(relative_path.read_text(encoding="utf-8"), namespace)
    return namespace

checks = []

# Lab 1: two revisions mutate the plan and conflict detection is explicit.
lab1a = load_module(root / "Lab_01_Agent_vs_Chatbot" / "assignment1.py")
lab1b = load_module(root / "Lab_01_Agent_vs_Chatbot" / "assignment2.py")
checks.append(("Lab 1 - two revisions without regeneration",
               lab1a["log"][3]["regenerated"] is False and lab1a["plan"]["Friday"]["time"] == "17:00-18:00"))
checks.append(("Lab 1 - scheduling conflict explicitly detected",
               lab1b["result"]["status"] == "CONFLICT"))

# Lab 2: low turnout notification and technical-event filtering.
lab2a = load_module(root / "Lab_02_Tool_Using_Agent" / "assignment1.py")
lab2b = load_module(root / "Lab_02_Tool_Using_Agent" / "assignment2.py")
average, trace = lab2a["answer"]([12, 9, 7])
checks.append(("Lab 2 - low turnout notification drafted",
               average < 10 and any(item["tool"] == "send_notification" for item in trace)))
checks.append(("Lab 2 - three-tool chain produced non-empty technical average",
               lab2b["average"] == 10.5 and lab2b["technical"][0]["category"] == "technical"))

# Lab 6: fourth task is rejected and third skill failure escalates.
lab6a = load_module(root / "Lab_06_OpenCLA_Runtime" / "assignment1.py")
lab6b = load_module(root / "Lab_06_OpenCLA_Runtime" / "assignment2.py")
fourth = lab6a["receive_task"]({"skill": "summarize", "text": "another note"}, "new-user")
fourth = lab6a["receive_task"]({"skill": "summarize", "text": "another note"}, "new-user")
for _ in range(2):
    fourth = lab6a["receive_task"]({"skill": "summarize", "text": "another note"}, "new-user")
checks.append(("Lab 6 - fourth task rejected",
               lab6a["receive_task"]({"skill": "summarize", "text": "fourth"}, "uday")["rejected"] is True))
escalated = lab6b["run_skill"]("draft_email", "test-user")
escalated = lab6b["run_skill"]("draft_email", "test-user")
escalated = lab6b["run_skill"]("draft_email", "test-user")
same_skill_result = lab6b["run_skill"]("summarize_notes", "test-user")
checks.append(("Lab 6 - repeated failure escalates",
               escalated.get("escalated") is True
               and same_skill_result.get("escalated") is not True))

# Lab 7: security scan and builder retry limits.
lab7a = load_module(root / "Lab_07_Agentic_Node_Graph" / "assignment1.py")
lab7b = load_module(root / "Lab_07_Agentic_Node_Graph" / "assignment2.py")
security_failure = lab7a["simulate_security"](True)
checks.append(("Lab 7 - security scan can fail and halt",
               security_failure[-1]["failure_behavior"] == "reject release"))
checks.append(("Lab 7 - builder never retries more than once",
               lab7b["builder"](2)["attempts"] == 2 and lab7b["builder"](2)["escalated"] is True))

# Lab 8: all four roles independently critique the merged draft.
lab8b = load_module(root / "Lab_08_Parallel_Swarm" / "assignment2.py")
role_critiques = lab8b["role_critiques"]
checks.append(("Lab 8 - every required role contributes independent critique",
               set(role_critiques) == {"research", "logistics", "budget", "judging"}
               and all(role_critiques[role] for role in role_critiques)))

# Lab 10: low-risk pod restart and rollback approval gate.
lab10b = load_module(root / "Lab_10_Cloud_Operations_Agent" / "assignment2.py")
lab10a = load_module(root / "Lab_10_Cloud_Operations_Agent" / "assignment1.py")
checks.append(("Lab 10 - low-risk action executes and rollback is gated",
               lab10b["execute"]("restart_single_pod")["action_executed"] is True
               and lab10b["execute"]("rollback")["action_executed"] is False))
checks.append(("Lab 10 - logs, deploy history, and metrics drive the database diagnosis",
               lab10a["severity"] == "degraded"
               and lab10a["incident_start"] == "09:15:00"
               and lab10a["diagnosis"]["suspect_deploy"]["version"] == "v3.2"))

# Lab 11: independent test catches deliberate CSV bug.
lab11b = load_module(root / "Lab_11_Agentic_SDLC_Factory" / "assignment2.py")
checks.append(("Lab 11 - deliberate bug is exposed by independent test",
               lab11b["tests"]["only_filtered_rows_present"] is False
               and "only_filtered_rows_present" in lab11b["failed_tests"]))

# Lab 12: cost omission and re-evaluation controls.
lab12a = load_module(root / "Lab_12_Safety_Evaluation_Governance" / "assignment1.py")
lab12b = load_module(root / "Lab_12_Safety_Evaluation_Governance" / "assignment2.py")
checks.append(("Lab 12 - omitted cost is rejected",
               lab12a["propose"](None)["rejected"] is True))
governed = lab12b["GovernedAgent"]()
for _ in range(5):
    governed.propose()
checks.append(("Lab 12 - sixth proposal is blocked until re-evaluation",
               governed.propose()["blocked"] is True))

# Lab 13: ALARM human gate and trend escalation.
lab13a = load_module(root / "Lab_13_Discipline_Specific_Agent" / "assignment1.py")
lab13b = load_module(root / "Lab_13_Discipline_Specific_Agent" / "assignment2.py")
checks.append(("Lab 13 - electrical ALARM requires human review",
               lab13a["safety"]("ALARM")["auto_execute"] is False))
checks.append(("Lab 13 - three WARNING readings escalate",
               lab13b["three_warning_escalation"](lab13b["modified_log"]) == "schedule_inspection"))

# Lab 14: two reusable skills and adversarial rejection.
lab14a = load_module(root / "Lab_14_Course_Project" / "assignment1.py")
lab14b = load_module(root / "Lab_14_Course_Project" / "assignment2.py")
checks.append(("Lab 14 - two skills route correctly",
               lab14a["password_reset_skill"]("I forgot my password")["skill"] == "password_reset"
               and lab14a["faq_triage"]("How do I connect to wifi?")["skill"] == "faq_triage"))
checks.append(("Lab 14 - adversarial instruction is rejected",
               all(result["correct_safety"] for result in lab14b["results"])))

failures = [name for name, passed in checks if not passed]
lines = [f"{'PASS' if passed else 'FAIL'}: {name}" for name, passed in checks]
lines.append(f"TOTAL: {len(checks) - len(failures)} passed, {len(failures)} failed")
print("\n".join(lines))
(root / "ASSIGNMENT_VERIFICATION.txt").write_text("\n".join(lines) + "\n", encoding="utf-8")
if failures:
    raise SystemExit(1)
