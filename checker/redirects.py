import requests

def count_redirects(url: str) -> int:
    try:
        r = requests.get(url, timeout=5, allow_redirects=True)
        return len(r.history)
    except Exception:
        return 0
