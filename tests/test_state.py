from app.services.state import load_last_state, save_last_state
from unittest.mock import mock_open, patch

def test_load_last_state_valid():
    with patch("builtins.open", mock_open(read_data="42")):
        assert load_last_state("dummy.txt") == 42

def test_load_last_state_invalid():
    with patch("builtins.open", side_effect=FileNotFoundError()):
        assert load_last_state("missing.txt") == 0

def test_save_last_state():
    m = mock_open()
    with patch("builtins.open", m):
        save_last_state(99, "output.txt")
        m.assert_called_once_with("output.txt", "w")
        m().write.assert_called_once_with("99")
