import urllib3
import json


slack_url = "https://hooks.slack.com/services/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"
http = urllib3.PoolManager()


def lambda_handler(event, context):
    msg = {
        "text": "SIIIIIIIIII, Ronaldoooooooo",
    }

    encoded_msg = json.dumps(msg).encode("utf-8")
    resp = http.request("POST", slack_url, body=encoded_msg)
    print(
        {
            "message": msg,
            "status_code": resp.status,
            "response": resp.data,
        }
    )