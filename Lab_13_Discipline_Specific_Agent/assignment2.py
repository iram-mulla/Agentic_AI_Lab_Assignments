modified_log = [{"vibration": 2.9}, {"vibration": 3.2}, {"vibration": 3.6}, {"vibration": 3.9}]

def three_warning_escalation(log):
    levels = ["WARNING" if 2.8 <= r["vibration"] < 4.5 else "NORMAL" for r in log]
    if len(levels) >= 3 and all(level == "WARNING" for level in levels[-3:]):
        return "schedule_inspection"
    return "continue_monitoring"

print({"log": modified_log, "recommendation": three_warning_escalation(modified_log)})
