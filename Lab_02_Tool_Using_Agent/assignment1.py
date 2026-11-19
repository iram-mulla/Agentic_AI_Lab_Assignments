def send_notification(message):
    return {"drafted": True, "message": message, "sent": False}

def answer(signups):
    average = sum(signups) / len(signups)
    trace = [{"tool": "calculator", "input": signups, "output": average, "reason": "determine whether low-turnout notice is justified"}]
    if average < 10:
        notice = send_notification("Low turnout detected. Promote the event and consider additional outreach.")
        trace.append({"tool": "send_notification", "input": notice["message"], "output": notice, "reason": "computed average fell below 10"})
        return average, trace
    return average, trace

average, trace = answer([12, 9, 7])
print({"average": average, "trace": trace})
