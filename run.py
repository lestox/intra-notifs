import os
import subprocess
import sys

REQUIRED_ENV_VARS = ["LOGIN", "PASSWORD"]

def has_valid_cookie():
    return os.path.isfile(".auth.env") and os.path.getsize(".auth.env") > 0

def has_valid_env():
    return all(os.getenv(var) for var in REQUIRED_ENV_VARS)

def try_refresh_cookie():
    print("[INFO] .auth.env is missing or empty — attempting to refresh...")
    try:
        subprocess.run(["python", "refresh_cookie.py"], check=True)
        if has_valid_cookie():
            print("[INFO] Cookie refreshed successfully.")
            return True
        else:
            print("[ERROR] Failed to obtain authenticator cookie. Aborting.")
            return False
    except Exception as e:
        print(f"[ERROR] Failed to run refresh_cookie.py: {e}")
        return False

if not has_valid_env():
    print("[FATAL] LOGIN or PASSWORD missing. Please check your .env file.")
    sys.exit(1)

if not has_valid_cookie():
    if not try_refresh_cookie():
        sys.exit(1)

subprocess.run(["python", "-m", "app"])
