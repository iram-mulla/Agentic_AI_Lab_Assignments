"""Cloud deployment failure diagnosis and approval-gated remediation."""
LOGS = [
    {"ts": "14:00:00", "level": "INFO", "msg": "deploy started payments-service v2.4.1"},
    {"ts": "14:00:45", "level": "INFO", "msg": "deploy completed payments-service v2.4.1"},
    {"ts": "14:03:40", "level": "ERROR", "msg": "refund endpoint: NullPointerException in RefundHandler"},
    {"ts": "14:04:05", "level": "ERROR", "msg": "refund endpoint: NullPointerException in RefundHandler"},
]
DEPLOY_HISTORY = [{"ts": "14:00:00", "service": "payments-service", "version": "v2.4.1", "prev_version": "v2.4.0"}]
METRICS = {"baseline_error_rate": 0.5, "current_error_rate": 1.6}

def classify_severity(metrics):
    ratio = metrics["current_error_rate"] / metrics["baseline_error_rate"]
    if ratio >= 2:
        return "degraded"
    return "early_warning"

def find_incident_start(logs):
    return next((entry["ts"] for entry in logs if entry["level"] == "ERROR"), None)

def correlate(logs, deploys, incident_start):
    deploy = deploys[0]
    return {
        "hypothesis": f"The {deploy['version']} deploy preceded refund errors starting at {incident_start}.",
        "suspect_deploy": deploy,
        "affected_path": "refund",
    }

def risk_level(action):
    return "high" if action in {"rollback", "delete", "config_change", "scale"} else "low"

def diagnose_and_propose(urgency_prompt=False):
    severity = classify_severity(METRICS)
    incident_start = find_incident_start(LOGS)
    hypothesis = correlate(LOGS, DEPLOY_HISTORY, incident_start)
    request = {
        "severity": severity,
        "diagnosis": hypothesis["hypothesis"],
        "proposed_action": "rollback",
        "status": "AWAITING HUMAN APPROVAL -- NOT EXECUTED",
    }
    if urgency_prompt:
        request["note"] = "Urgency noted, but approval is still required."
    assert "action_executed" not in request
    return request

if __name__ == "__main__":
    print(diagnose_and_propose(urgency_prompt=True))
