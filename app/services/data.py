import requests

def get_data(url, cookie):
    headers = {
        "Cookie": cookie,
        "User-Agent": "curl/7.81.0"
    }

    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        raise Exception(f"GET {url} failed: {response.status_code} - {response.text}")

    try:
        return response.json()
    except Exception:
        raise Exception(f"Failed to parse JSON from {url}: {response.text}")
