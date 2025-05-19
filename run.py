import subprocess
import os
import sys


def has_valid_cookie():
    return os.path.isfile(".auth.env") and os.path.getsize(".auth.env") > 0


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


if not has_valid_cookie():
    if not try_refresh_cookie():
        sys.exit(1)

subprocess.run(["python", "-m", "app"])
