class GovernedAgent:
    def __init__(self): self.proposals, self.validated = 0, True
    def evaluate(self): self.validated = True
    def propose(self):
        if self.proposals >= 5 and not self.validated:
            return {"blocked": True, "reason": "re-evaluation required"}
        self.proposals += 1
        if self.proposals % 5 == 0:
            self.validated = False
        return {"proposed": True}

agent = GovernedAgent()
for i in range(5):
    print(f"proposal_{i + 1}", agent.propose())
print("proposal_6", agent.propose())
agent.evaluate()
print("proposal_6_after_re_evaluation", agent.propose())
