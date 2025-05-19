import os
import requests
from dotenv import load_dotenv

load_dotenv()

LOGIN = os.getenv("LOGIN")
PASSWORD = os.getenv("PASSWORD")
AUTH_URL = "https://auth.etna-alternance.net/identity"

if not LOGIN or not PASSWORD:
    print("[ERROR] LOGIN or PASSWORD missing in .env")
    exit(1)

headers = {
    "Content-Type": "application/json",
    "User-Agent": "curl/8.13.0"
}

payload = {
    "login": LOGIN,
    "password": PASSWORD
}

try:
    response = requests.post(AUTH_URL, headers=headers, json=payload)
    set_cookie = response.headers.get("Set-Cookie", "")

    if "authenticator=" not in set_cookie:
        print("[ERROR] No authenticator cookie found in response headers")
        exit(1)

    token = set_cookie.split("authenticator=")[1].split(";")[0]

    with open(".auth.env", "w") as f:
        f.write(f"authenticator={token}")

    print("[INFO] Cookie refreshed successfully.")
except Exception as e:
    print(f"[ERROR] Exception while refreshing cookie: {e}")
    exit(1)
