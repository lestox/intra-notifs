def read_cookie(path: str = ".auth.env") -> str | None:
    try:
        with open(path) as f:
            return f.read().strip()
    except FileNotFoundError:
        return None
