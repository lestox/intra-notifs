import subprocess
import json
import re
from app.constants.auth import auth


def authenticate():
    credentials_json = json.dumps(
        {"login": auth["login"], "password": auth["password"]}
    )

    curl_cmd = [
        "curl",
        "-i",
        "-s",
        "-X",
        "POST",
        auth["url"] + "/identity",
        "-H",
        "Content-Type: application/json",
        "-A",
        "curl/8.13.0",
        "-d",
        credentials_json,
    ]

    try:
        result = subprocess.check_output(curl_cmd, text=True)
    except subprocess.CalledProcessError as e:
        raise Exception(f"Curl command failed: {e.output}")

    split_marker = "\r\n\r\n" if "\r\n\r\n" in result else "\n\n"
    headers_part, body_part = result.split(split_marker, 1)

    match = re.search(
        r"[Ss]et-[Cc]ookie:\s*authenticator=\"?([^\";\n\r]+)\"?", headers_part
    )
    if not match:
        raise Exception("No authenticator cookie found in headers")

    cookie = f"authenticator={match.group(1)}"

    try:
        data = json.loads(body_part)
    except Exception:
        raise Exception(f"Failed to parse JSON body: {body_part}")

    if "login" in data and "id" in data:
        return cookie, data
    else:
        raise Exception(f"Authentication JSON invalid: {data}")
