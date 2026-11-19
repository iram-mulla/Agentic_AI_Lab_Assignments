# Agentic AI Systems — Final Run and Demo Guide

## 1. Project overview

This workspace contains 14 lab folders for the Agentic AI Systems lab guide. Each lab folder has a `reference.py`, `assignment1.py`, and `assignment2.py`. Lab 14 also contains the Campus Help-Desk capstone source code.

The lab programs use local, deterministic, rule-based stand-ins. They do not require an external LLM or API key.

## 2. Environment setup

Open PowerShell in the project root:

```powershell
Set-Location "D:\Engineering\7th sem\Agentic AI\Agentic-AI-Lab-Assignments"
```.\.venv\Scripts\python.exe --version

Check the workspace virtual environment:

```powershell
Test-Path ".\.venv\Scripts\python.exe"
.\.venv\Scripts\python.exe --version
.\.venv\Scripts\python.exe -m pip --version
```

If the virtual environment is missing or unusable:

```powershell
py -3 -m venv .venv
.\.venv\Scripts\python.exe -m pip install --upgrade pip
```

## 3. Dependency installation

The lab files use only the Python standard library. ReportLab is only needed by the optional PDF generator, not by the lab assignments.

```powershell
.\.venv\Scripts\python.exe -m pip install -r .\requirements.txt
```

## 4. Full testing commands

Run every reference and assignment file:

```powershell
.\.venv\Scripts\python.exe .\run_lab_tests.py
```

Run the focused rubric verification:

```powershell
.\.venv\Scripts\python.exe .\verify_assignments.py
```

The full runner writes:

- `PROGRESS.md`
- `Lab_XX_Name\TEST_OUTPUT.txt` in every lab folder
- `ASSIGNMENT_VERIFICATION.txt`

## 5. Individual run commands

### Lab 1 — Agent vs Chatbot

```powershell
.\.venv\Scripts\python.exe ".\Lab_01_Agent_vs_Chatbot\reference.py"
.\.venv\Scripts\python.exe ".\Lab_01_Agent_vs_Chatbot\assignment1.py"
.\.venv\Scripts\python.exe ".\Lab_01_Agent_vs_Chatbot\assignment2.py"
```

### Lab 2 — Tool-Using Agent

```powershell
.\.venv\Scripts\python.exe ".\Lab_02_Tool_Using_Agent\reference.py"
.\.venv\Scripts\python.exe ".\Lab_02_Tool_Using_Agent\assignment1.py"
.\.venv\Scripts\python.exe ".\Lab_02_Tool_Using_Agent\assignment2.py"
```

### Lab 3 — Skill Creation

```powershell
.\.venv\Scripts\python.exe ".\Lab_03_Skill_Creation\reference.py"
.\.venv\Scripts\python.exe ".\Lab_03_Skill_Creation\assignment1.py"
.\.venv\Scripts\python.exe ".\Lab_03_Skill_Creation\assignment2.py"
```

### Lab 4 — Memory and Retrieval

```powershell
.\.venv\Scripts\python.exe ".\Lab_04_Memory_and_Retrieval\reference.py"
.\.venv\Scripts\python.exe ".\Lab_04_Memory_and_Retrieval\assignment1.py"
.\.venv\Scripts\python.exe ".\Lab_04_Memory_and_Retrieval\assignment2.py"
```

### Lab 5 — MCP-Style Connector

```powershell
.\.venv\Scripts\python.exe ".\Lab_05_MCP_Style_Connector\reference.py"
.\.venv\Scripts\python.exe ".\Lab_05_MCP_Style_Connector\assignment1.py"
.\.venv\Scripts\python.exe ".\Lab_05_MCP_Style_Connector\assignment2.py"
```

### Lab 6 — OpenCLA/OpenClaw Runtime

```powershell
.\.venv\Scripts\python.exe ".\Lab_06_OpenCLA_Runtime\reference.py"
.\.venv\Scripts\python.exe ".\Lab_06_OpenCLA_Runtime\assignment1.py"
.\.venv\Scripts\python.exe ".\Lab_06_OpenCLA_Runtime\assignment2.py"
```

### Lab 7 — Agentic Node Graph

```powershell
.\.venv\Scripts\python.exe ".\Lab_07_Agentic_Node_Graph\reference.py"
.\.venv\Scripts\python.exe ".\Lab_07_Agentic_Node_Graph\assignment1.py"
.\.venv\Scripts\python.exe ".\Lab_07_Agentic_Node_Graph\assignment2.py"
```

### Lab 8 — Parallel Swarm

```powershell
.\.venv\Scripts\python.exe ".\Lab_08_Parallel_Swarm\reference.py"
.\.venv\Scripts\python.exe ".\Lab_08_Parallel_Swarm\assignment1.py"
.\.venv\Scripts\python.exe ".\Lab_08_Parallel_Swarm\assignment2.py"
```

### Lab 9 — Deep Research Agent

```powershell
.\.venv\Scripts\python.exe ".\Lab_09_Deep_Research_Agent\reference.py"
.\.venv\Scripts\python.exe ".\Lab_09_Deep_Research_Agent\assignment1.py"
.\.venv\Scripts\python.exe ".\Lab_09_Deep_Research_Agent\assignment2.py"
```

### Lab 10 — Cloud Operations Agent

```powershell
.\.venv\Scripts\python.exe ".\Lab_10_Cloud_Operations_Agent\reference.py"
.\.venv\Scripts\python.exe ".\Lab_10_Cloud_Operations_Agent\assignment1.py"
.\.venv\Scripts\python.exe ".\Lab_10_Cloud_Operations_Agent\assignment2.py"
```

### Lab 11 — Agentic SDLC Factory

```powershell
.\.venv\Scripts\python.exe ".\Lab_11_Agentic_SDLC_Factory\reference.py"
.\.venv\Scripts\python.exe ".\Lab_11_Agentic_SDLC_Factory\assignment1.py"
.\.venv\Scripts\python.exe ".\Lab_11_Agentic_SDLC_Factory\assignment2.py"
```

### Lab 12 — Safety, Evaluation, and Governance

```powershell
.\.venv\Scripts\python.exe ".\Lab_12_Safety_Evaluation_Governance\reference.py"
.\.venv\Scripts\python.exe ".\Lab_12_Safety_Evaluation_Governance\assignment1.py"
.\.venv\Scripts\python.exe ".\Lab_12_Safety_Evaluation_Governance\assignment2.py"
```

### Lab 13 — Discipline-Specific Engineering Agent

```powershell
.\.venv\Scripts\python.exe ".\Lab_13_Discipline_Specific_Agent\reference.py"
.\.venv\Scripts\python.exe ".\Lab_13_Discipline_Specific_Agent\assignment1.py"
.\.venv\Scripts\python.exe ".\Lab_13_Discipline_Specific_Agent\assignment2.py"
```

### Lab 14 — Capstone Project Studio

```powershell
.\.venv\Scripts\python.exe ".\Lab_14_Course_Project\reference.py"
.\.venv\Scripts\python.exe ".\Lab_14_Course_Project\assignment1.py"
.\.venv\Scripts\python.exe ".\Lab_14_Course_Project\assignment2.py"
.\.venv\Scripts\python.exe ".\Lab_14_Course_Project\source_code\campus_helpdesk.py"
```

## 6. Expected behavior by assignment

| Lab | Assignment 1 | Assignment 2 |
|---|---|---|
| 1 | Tuesday and Friday revisions mutate the same plan; log shows separate rounds. | Wednesday conflict is reported explicitly. |
| 2 | Average below threshold causes a drafted notification; no notification is sent. | CSV is read, technical rows are filtered, average is calculated. |
| 3 | Competing claims are compared and one supported claim is selected explicitly. | Missing evidence and limitation fields become `not stated in source`. |
| 4 | Database and hosting records remain isolated. | Fresh records are used normally; records older than 30 days receive a warning. |
| 5 | `list_files` appears in discovery and is called through the client. | `/etc/passwd` or another outside path is rejected by the safe-directory guard. |
| 6 | Three tasks succeed; the fourth task is rejected. | Two failures are recorded; a third attempt escalates instead of retrying. |
| 7 | Security scan succeeds or rejects release on a critical finding. | Builder succeeds after one retry or escalates after two failures. |
| 8 | Marketing cost is compared with the overall budget cap. | Logistics, marketing, and research each produce independent objections. |
| 9 | S1/S4 are represented as a direct contradiction. | Claims are ranked by source-quality tier while the lower-tier claim remains visible. |
| 10 | Database pool exhaustion produces a distinct diagnosis and severity. | A pod restart is auto-executable; rollback remains approval-gated. |
| 11 | CSV and PDF stories have separate design/code/test lineage. | A deliberately inverted filter is caught by an independent test. |
| 12 | Missing cost and over-budget proposals are rejected as applicable. | Proposal 6 is blocked until re-evaluation. |
| 13 | Electrical ALARM is routed to human review. | Three consecutive warnings escalate to inspection. |
| 14 | FAQ triage and password-reset are separate reusable skills. | Five adversarial/normal cases verify routing and safety. |

## 7. Lab-by-lab demonstration

### Lab 1 — Agent vs Chatbot

- Concept: Goal-plan-act-observe-revise loop.
- Assignment 1: two independent mutations of one plan.
- Assignment 2: scheduling conflict detection.
- Open: `Lab_01_Agent_vs_Chatbot\assignment1.py`, then `assignment2.py`.
- Command: run the two assignment commands above.
- Show: the log has two revise iterations and no regeneration; the conflict JSON lists Wednesday.
- Explain: this is agent behavior because it tracks state, acts, observes, revises, and stops on a predicate.
- Viva: What is the stopping condition? Why mutate rather than rerun?

### Lab 2 — Tool-Using Agent

- Concept: structured tool calling and traceable results.
- Assignment 1: notification drafting below a threshold.
- Assignment 2: read CSV, filter category, calculate average.
- Open: `Lab_02_Tool_Using_Agent\assignment1.py` and `assignment2.py`.
- Show: notification is only drafted, and technical average is 10.5.
- Explain: tool inputs and outputs are structured; the notification is never sent.
- Viva: Why is tool chaining useful? How are tool errors handled?

### Lab 3 — Skill Creation

- Concept: reusable skill contract.
- Assignment 1: competing-claim selection.
- Assignment 2: low-evidence source handling.
- Open: the two assignment files.
- Show: explicit selection note and `not stated in source`.
- Explain: the skill preserves output structure and avoids fabrication.
- Viva: What makes a skill reusable? How does it handle missing evidence?

### Lab 4 — Memory and Retrieval

- Concept: scoped memory, source tagging, write permissions, staleness.
- Assignment 1: database/hosting isolation.
- Assignment 2: 30-day staleness warning.
- Open: the two assignment files.
- Show: hosting fact never appears in database retrieval; 90-day fact is stale.
- Explain: memory retrieval is scoped by topic and checked for age.
- Viva: Session memory vs stored memory? Why conflict detection matters?

### Lab 5 — MCP-Style Connector

- Concept: capability discovery, resources, tools, permission boundaries.
- Assignment 1: discoverable `list_files`.
- Assignment 2: safe-directory enforcement.
- Open: `assignment1.py` and `assignment2.py`.
- Show: discovery manifest plus file list; outside `/safe/` returns structured error.
- Explain: MCP-style clients discover capabilities instead of hard-coding every method.
- Viva: Resource vs tool? How is the database caller restricted?

### Lab 6 — OpenCLA/OpenClaw Runtime

- Concept: skill registry, runtime loop, scoped memory, audit log.
- Assignment 1: three-task rate limit.
- Assignment 2: escalation after repeated skill failure.
- Open: `assignment1.py` and `assignment2.py`.
- Show: fourth attempt is rejected; third attempt escalates.
- Explain: the core skill dispatch remains separate from runtime controls.
- Viva: Where is per-user state stored? How is an escalation decided?

### Lab 7 — Agentic Node Graph

- Concept: graph nodes with owners, success criteria, and failure paths.
- Assignment 1: security scan.
- Assignment 2: builder retry limit.
- Open: `assignment1.py` and `assignment2.py`.
- Show: critical security finding stops release; builder fails twice and escalates.
- Explain: graph execution stops at failure and uses an explicit recovery behavior.
- Viva: Why does each node need success criteria and an on-failure path?

### Lab 8 — Parallel Swarm

- Concept: independent role agents run in parallel and merge through critique/resolution.
- Assignment 1: marketing role and budget conflict.
- Assignment 2: distributed critique.
- Open: `assignment1.py` and `assignment2.py`.
- Show: marketing conflict and objections by multiple roles.
- Explain: merge and critique are separate stages; conflicts are logged.
- Viva: When should agents be parallel? How are priorities resolved?

### Lab 9 — Deep Research Agent

- Concept: evidence extraction, comparison, and traceable synthesis.
- Assignment 1: contradictory S1/S4 source.
- Assignment 2: source-quality weighting.
- Open: `assignment1.py` and `assignment2.py`.
- Show: direct contradiction, reason, quality tiers, and trace.
- Explain: lower-quality claims are disclosed and down-weighted, not discarded.
- Viva: Conflict vs gap? Why should synthesis remain traceable?

### Lab 10 — Cloud Operations Agent

- Concept: severity, correlation, risk classification, approval gate.
- Assignment 1: database pool exhaustion scenario.
- Assignment 2: pod restart vs rollback behavior.
- Open: `assignment1.py` and `assignment2.py`.
- Show: degraded database incident and low-risk auto execution versus rollback approval.
- Explain: urgency does not bypass approval for destructive or rollback actions.
- Viva: What is high risk? How is severity classified?

### Lab 11 — Agentic SDLC Factory

- Concept: requirement, design, implementation, independent tests, review, release.
- Assignment 1: concurrent story lineage.
- Assignment 2: deliberate implementation bug caught by tests.
- Open: `assignment1.py` and `assignment2.py`.
- Show: two story-specific artifact chains and failing filtered-row test.
- Explain: tests are generated from acceptance criteria and do not import implementation.
- Viva: Why must testing be independent? Where are the human checkpoints?

### Lab 12 — Safety, Evaluation, and Governance

- Concept: least privilege, evaluation, human approval, privacy, rollback, audit.
- Assignment 1: cost budget control.
- Assignment 2: mandatory re-evaluation after five proposals.
- Open: `assignment1.py` and `assignment2.py`.
- Show: omitted and over-budget costs rejected; sixth proposal blocked.
- Explain: the agent cannot approve or apply production changes itself.
- Viva: What evidence is mandatory? What privileged process applies approved changes?

### Lab 13 — Discipline-Specific Engineering Agent

- Concept: applying agent patterns to electrical/mechanical engineering safety.
- Assignment 1: electrical load ALARM.
- Assignment 2: three warning readings.
- Open: `assignment1.py` and `assignment2.py`.
- Show: ALARM has `auto_execute: false`; three warnings schedule inspection.
- Explain: safety thresholds and trend escalation are separate from automatic shutdown.
- Viva: Why is an ALARM human-reviewed? Why monitor trends as well as thresholds?

### Lab 14 — Capstone Project Studio

- Concept: integrated node graph, tools, skills, memory, audit, evaluation, and safety.
- Assignment 1: FAQ and password-reset skills.
- Assignment 2: expanded adversarial evaluation.
- Open: `Lab_14_Course_Project\assignment1.py`, `assignment2.py`, and `source_code\campus_helpdesk.py`.
- Command: run the three or four commands shown above.
- Show: two skill routes, escalation, adversarial rejection, and five-case evaluation.
- Explain: the source combines intake, triage, memory, logging, tools, and safety.
- Viva: What are the limitations? Which component would you replace for a real deployment?

## 8. Suggested speaking script

### Short introduction

"I have implemented all 14 labs as runnable Python programs. The demonstrations cover the core agentic concepts: goal loops, tools, reusable skills, memory, MCP-style connectors, runtime registries, node graphs, parallel swarms, evidence synthesis, operations safety, SDLC automation, governance, discipline-specific engineering, and an integrated capstone worklet. I use the workspace virtual environment and local rule-based stand-ins, so the programs run without external API keys."

### During the demonstrations

"This output comes from the assignment file, not a static slide. It shows the required state change or failure behavior. The key design choice is that the safety or stopping condition is explicit and observable."

### Conclusion

"The full runner executes every reference and assignment. The focused verification separately checks the rubric-sensitive scenarios such as conflicts, escalation, safety gates, and deliberate failures. Execution evidence is saved in `PROGRESS.md`, `ASSIGNMENT_VERIFICATION.txt`, and each lab's `TEST_OUTPUT.txt`."

## 9. Suggested viva questions and answers

- **What makes an agent different from a chatbot?** It maintains goals and state, chooses actions, observes results, and revises until a stopping condition is met.
- **Why use tool schemas?** They define inputs and outputs, reduce ambiguity, and allow validation before propagation.
- **Why keep memory scoped?** It prevents facts from unrelated topics or users leaking into answers.
- **What is MCP-style discovery?** The client asks the server for a capability manifest instead of assuming every capability exists.
- **Why use a skill registry?** New skills can be registered without rewriting the runtime dispatch loop.
- **How does a node graph handle failure?** Each node has success criteria and an explicit failure route.
- **How are swarm conflicts resolved?** The merge is critiqued against role constraints; the final resolution follows a named priority rule.
- **How is evidence synthesis traceable?** Each output is tagged with source IDs and retains evidence and limitation fields.
- **Why must cloud rollback require approval?** Rollback can interrupt service or worsen an incident, so it is high risk.
- **Why are tests independent of coding agents?** Independence prevents tests from validating implementation behavior merely because the implementation generated them.
- **What governance controls are essential?** Least privilege, evaluation, human approval, privacy scrubbing, rollback, and audit logs.
- **Why can an ALARM not auto-execute?** An engineering shutdown or isolation action can create physical or operational risk.
- **What is missing in the capstone?** The repository template uses local mock storage and keyword matching; production would use persistent storage, authentication, semantic retrieval, and real ticket APIs.

## 10. Suggested 5–7 most important demonstrations

1. Lab 1 Assignment 1 — two revisions and mutation of the same plan.
2. Lab 6 Assignment 1 — runtime rate limit.
3. Lab 7 Assignment 2 — builder retry and escalation.
4. Lab 10 Assignment 2 — low-risk action versus rollback approval gate.
5. Lab 11 Assignment 2 — independent test catches a deliberate bug.
6. Lab 12 Assignments 1 and 2 — cost and re-evaluation governance.
7. Lab 14 — integrated campus help-desk demo and adversarial safety case.

## 11. Final submission checklist

- [ ] Virtual environment exists and starts.
- [ ] Dependencies install successfully.
- [ ] Full test runner returns 43 passed.
- [ ] Rubric verification returns 16 passed.
- [ ] `PROGRESS.md` is present.
- [ ] `ASSIGNMENT_VERIFICATION.txt` is present.
- [ ] Every lab has `reference.py`, `assignment1.py`, and `assignment2.py`.
- [ ] Every lab's `TEST_OUTPUT.txt` is present.
- [ ] Course project report is not modified by lab audit work.
- [ ] Individual commands have been practiced once.

## 12. Final audit status and remaining issues

### Test status observed

- Full runner rerun: 43 Python files executed, 43 passed, 0 failed.
- Rubric verification rerun: 16 checks passed, 0 failed.
- The runner was corrected to ignore non-directory `Lab_*` matches before the final rerun.

### Remaining implementation-level caveats

- Lab 3 Assignment 1 uses an explicit rule-based claim selection heuristic, not an external LLM. This matches the lab guide's offline rule-based model.
- Lab 6 Assignment 2 uses a local audit list and explicitly counts prior error entries; it demonstrates the requirement but is not connected to the full runtime in that one file.
- Lab 10 Assignment 1 demonstrates a distinct database-pool incident, severity, and diagnosis, but the implementation is a compact scenario rather than the guide's full log/correlation tool chain.
- Several assignments are deterministic demonstrations with fixed scenario data. They are complete for laboratory demonstration and grading, but would require live databases, real APIs, or LLM calls for production use.
- Lab 14 uses in-memory ticket storage and keyword FAQ matching, as disclosed in its source limitations.

No course-project report file was overwritten during this audit.
