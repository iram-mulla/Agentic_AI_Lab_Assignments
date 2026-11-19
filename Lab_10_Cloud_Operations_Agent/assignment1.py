database_incident = {
    "logs": [
        {"level": "INFO", "ts": "09:00:00", "msg": "deploy started: user-api v3.2"},
        {"level": "INFO", "ts": "09:01:00", "msg": "deploy completed: user-api v3.2"},
        {"level": "WARN", "ts": "09:14:00", "msg": "database connection pool utilization elevated"},
        {"level": "ERROR", "ts": "09:15:00", "msg": "database connection pool exhausted"},
        {"level": "ERROR", "ts": "09:15:30", "msg": "database connection acquisition timeout"},
    ],
    "deploy_history": [
        {
            "ts": "09:01:00",
            "service": "user-api",
            "version": "v3.2",
            "previous_version": "v3.1",
        }
    ],
    "metrics": {
        "baseline_error_rate": 0.2,
        "current_error_rate": 3.5,
    },
}


def classify_severity(metrics):
    ratio = metrics["current_error_rate"] / metrics["baseline_error_rate"]
    if metrics["current_error_rate"] > 50:
        return "down"
    if ratio >= 2:
        return "degraded"
    return "early_warning"


def find_incident_start(logs):
    return next(entry["ts"] for entry in logs if entry["level"] == "ERROR")


def correlate_with_deploy(logs, deploy_history, incident_start):
    error_text = " ".join(
        entry["msg"].lower()
        for entry in logs
        if entry["level"] in {"WARN", "ERROR"}
    )
    affected = "database connection pool" if "database" in error_text else "unknown"
    recent_deploy = max(
        (deploy for deploy in deploy_history if deploy["ts"] < incident_start),
        key=lambda deploy: deploy["ts"],
    )
    return {
        "affected_path": affected,
        "suspect_deploy": recent_deploy,
        "hypothesis": (
            f"The incident began at {incident_start}, shortly after "
            f"{recent_deploy['service']} deployed {recent_deploy['version']} "
            f"at {recent_deploy['ts']}. The warnings and errors are concentrated "
            f"in the {affected}, consistent with a release-related pool regression."
        ),
    }


severity = classify_severity(database_incident["metrics"])
incident_start = find_incident_start(database_incident["logs"])
diagnosis = correlate_with_deploy(
    database_incident["logs"],
    database_incident["deploy_history"],
    incident_start,
)

print({
    "severity": severity,
    "incident_start": incident_start,
    "current_error_rate": database_incident["metrics"]["current_error_rate"],
    "baseline_error_rate": database_incident["metrics"]["baseline_error_rate"],
    "diagnosis": diagnosis,
})
