from app.services.state import load_last_state, save_last_state


def test_state_read_write(tmp_path):
    state_file = tmp_path / "last_seen.txt"
    save_last_state(5, str(state_file))
    assert load_last_state(str(state_file)) == 5


def test_state_missing_returns_zero():
    assert load_last_state("nonexistent.txt") == 0
