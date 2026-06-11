alerts = []

def create_alert(

    title,

    severity

):

    alert = {

        "title": title,

        "severity": severity

    }

    alerts.append(alert)

    return alert