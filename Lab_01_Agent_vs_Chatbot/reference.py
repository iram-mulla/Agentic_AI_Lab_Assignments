import json

class StudyPlannerAgent:
    def __init__(self, existing_schedule):
        self.goal = {"subjects": None, "hours_per_day": None, "unavailable_days": None, "schedule_generated": False}
        self.existing_schedule = existing_schedule
        self.plan = None
        self.log = []

    def satisfied(self):
        return self.goal["schedule_generated"]

    def next_step(self):
        for field in ("subjects", "hours_per_day", "unavailable_days"):
            if self.goal[field] is None:
                return "ask", field
        return "generate_plan", None

    def run(self):
        answers = {"subjects": ["Data Structures", "Operating Systems", "AI Agents"], "hours_per_day": 2, "unavailable_days": ["Sunday"]}
        while not self.satisfied():
            step, arg = self.next_step()
            if step == "ask":
                self.goal[arg] = answers[arg]
                self.log.append({"iteration": len(self.log) + 1, "planned": f"ask for {arg}", "action": f"asked user for {arg}", "observed": answers[arg], "stopped": False})
            else:
                busy = self.existing_schedule
                days = [d for d in ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"] if d not in self.goal["unavailable_days"]]
                self.plan = {}
                for i, day in enumerate(days):
                    time = "20:00-22:00" if day in busy.get("busy_days", []) else "17:00-19:00"
                    self.plan[day] = {"subject": self.goal["subjects"][i % 3], "time": time}
                self.goal["schedule_generated"] = True
                self.log.append({"iteration": len(self.log) + 1, "planned": "generate schedule", "action": "built weekly plan", "observed": self.plan, "stopped": True, "stop_reason": "schedule_generated is True"})
        return self.plan

    def revise(self, feedback):
        if "tuesday" in feedback.lower() and "evening" in feedback.lower():
            self.plan["Tuesday"]["time"] = "20:00-22:00"
        return self.plan

if __name__ == "__main__":
    agent = StudyPlannerAgent({"busy_days": ["Wednesday"]})
    print(json.dumps(agent.run(), indent=2))
    print(json.dumps(agent.revise("Move Tuesday's session to the evening"), indent=2))
