def load_last_state(path: str = "last_seen_count.txt") -> int:
    try:
        with open(path) as f:
            return int(f.read())
    except (FileNotFoundError, ValueError):
        return 0


def save_last_state(count: int, path: str = "last_seen_count.txt") -> None:
    with open(path, "w") as f:
        f.write(str(count))
