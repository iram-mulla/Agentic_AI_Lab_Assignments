"""Mechanical predictive-maintenance engineering agent."""
SENSOR_LOG = [
    {"t": 0, "vibration_mm_s": 1.8, "temp_c": 61},
    {"t": 1, "vibration_mm_s": 1.9, "temp_c": 62},
    {"t": 2, "vibration_mm_s": 2.4, "temp_c": 65},
    {"t": 3, "vibration_mm_s": 3.1, "temp_c": 70},
    {"t": 4, "vibration_mm_s": 4.6, "temp_c": 76},
    {"t": 5, "vibration_mm_s": 6.2, "temp_c": 84},
]
THRESHOLDS = {"vibration_warn": 2.8, "vibration_alarm": 4.5, "temp_warn": 70, "temp_alarm": 80}

def classify_condition(reading):
    if reading["vibration_mm_s"] >= THRESHOLDS["vibration_alarm"] or reading["temp_c"] >= THRESHOLDS["temp_alarm"]:
        return "ALARM"
    if reading["vibration_mm_s"] >= THRESHOLDS["vibration_warn"] or reading["temp_c"] >= THRESHOLDS["temp_warn"]:
        return "WARNING"
    return "NORMAL"

def trend_direction(log):
    deltas = [log[index + 1]["vibration_mm_s"] - log[index]["vibration_mm_s"] for index in range(len(log) - 1)]
    return "worsening" if all(delta >= 0 for delta in deltas) else "mixed"

def safety_check(condition):
    if condition == "ALARM":
        return {"action_allowed": "recommend_shutdown_for_human_review", "auto_execute": False}
    if condition == "WARNING":
        return {"action_allowed": "schedule_inspection", "auto_execute": False}
    return {"action_allowed": "continue_monitoring", "auto_execute": True}

def predictive_maintenance_agent(log=SENSOR_LOG):
    latest = log[-1]
    condition = classify_condition(latest)
    safety = safety_check(condition)
    return {
        "domain": "Mechanical Engineering -- Predictive Maintenance",
        "latest_reading": latest,
        "condition": condition,
        "trend": trend_direction(log),
        "recommended_action": safety["action_allowed"],
        "auto_executed": safety["auto_execute"],
        "evaluation_method": "ISO-10816-style threshold bands cross-checked with temperature trend.",
    }

if __name__ == "__main__":
    result = predictive_maintenance_agent()
    print(result)
    assert result["condition"] != "ALARM" or result["auto_executed"] is False
