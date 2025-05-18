import subprocess
import json
from constants.auth import auth

def authenticate():
    credentials_json = json.dumps({
        "login": auth["login"],
        "password": auth["password"]
    })

    curl_cookie_cmd = [
        "curl", "-s", "-c", "-", "-X", "POST", auth['url'] + "/identity",
        "-H", "Content-Type: application/json",
        "-d", credentials_json
    ]

    cookie_result = subprocess.check_output(curl_cookie_cmd, text=True)
    cookie_line = next((line for line in cookie_result.splitlines() if "authenticator" in line), None)

    if not cookie_line:
        raise Exception("No authenticator cookie found")

    cookie_parts = cookie_line.split()
    cookie = f"{cookie_parts[-2]}={cookie_parts[-1]}"

    curl_json_cmd = [
        "curl", "-s", "-X", "POST", auth['url'] + "/identity",
        "-H", "Content-Type: application/json",
        "-d", credentials_json
    ]

    json_result = subprocess.check_output(curl_json_cmd, text=True)

    try:
        data = json.loads(json_result)
    except Exception:
        raise Exception(f"Failed to parse JSON from response: {json_result}")

    if 'login' in data and 'id' in data:
        return cookie, data
    else:
        raise Exception(f"Authentication response invalid: {data}")
