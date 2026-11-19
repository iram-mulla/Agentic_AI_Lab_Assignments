"""Governance guardrails for production-change proposals."""
REGRESSION_SUITE_RESULT = {"passed": 9, "total": 10}

class ProdChangeAgent:
    permissions = {"can_write": "staging_only"}

    def __init__(self):
        self.audit_log = []
        self.evaluated = False
        self.proposal_count = 0

    def evaluate(self):
        pass_rate = REGRESSION_SUITE_RESULT["passed"] / REGRESSION_SUITE_RESULT["total"]
        self.evaluated = pass_rate >= 0.8
        self.audit_log.append({"step": "evaluation", "pass_rate": pass_rate, "passed": self.evaluated})
        return self.evaluated

    def propose_change(self, diagnosis, action, rollback_plan, privacy_scrubbed, cost_estimate=None, finance_approved=False):
        if not self.evaluated:
            return {"rejected": True, "reason": "evaluation gate not passed"}
        if self.permissions["can_write"] != "staging_only":
            raise PermissionError("Agent must not hold direct production write access.")
        if not rollback_plan:
            return {"rejected": True, "reason": "No rollback plan defined"}
        if not privacy_scrubbed:
            return {"rejected": True, "reason": "Diagnostic input was not privacy-scrubbed"}
        if cost_estimate is None:
            return {"rejected": True, "reason": "Cost estimate is required"}
        if cost_estimate > 10000 and not finance_approved:
            return {"rejected": True, "reason": "Cost exceeds budget without finance approval"}
        if self.proposal_count >= 5:
            return {"rejected": True, "reason": "Re-evaluation required after every 5 proposals"}
        self.proposal_count += 1
        request = {"diagnosis": diagnosis, "proposed_action": action, "rollback_plan": rollback_plan, "requires_approval": True}
        self.audit_log.append({"step": "approval_requested", "data": request})
        return request

    def apply_after_approval(self, request, human_decision):
        if human_decision != "approved":
            return {"applied": False, "reason": "not approved"}
        return {"applied": False, "handed_off_to": "privileged_deploy_process"}

if __name__ == "__main__":
    agent = ProdChangeAgent()
    print(agent.evaluate())
    print(agent.propose_change("memory leak", "revert config", None, True, 500))
    print(agent.propose_change("memory leak", "revert config", "revert to v3", True, 500))
