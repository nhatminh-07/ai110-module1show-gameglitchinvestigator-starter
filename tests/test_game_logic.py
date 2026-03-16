import pytest

from logic_utils import check_guess, get_range_for_difficulty, parse_guess, update_score


@pytest.mark.parametrize(
    ("difficulty", "expected_range"),
    [
        ("Easy", (1, 20)),
        ("Normal", (1, 100)),
        ("Hard", (1, 50)),
        ("Unknown", (1, 100)),
    ],
)
def test_get_range_for_difficulty(difficulty, expected_range):
    assert get_range_for_difficulty(difficulty) == expected_range


@pytest.mark.parametrize(
    ("raw", "expected"),
    [
        (None, (False, None, "Enter a guess.")),
        ("", (False, None, "Enter a guess.")),
        ("   ", (False, None, "Enter a guess.")),
        ("abc", (False, None, "That is not a whole number.")),
        ("10.5", (False, None, "That is not a whole number.")),
        ("42", (True, 42, None)),
        (" 7 ", (True, 7, None)),
        ("-3", (True, -3, None)),
    ],
)
def test_parse_guess(raw, expected):
    assert parse_guess(raw) == expected


def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    result, message = check_guess(50, 50)
    assert result == "Win"
    assert message == "🎉 Correct!"


def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    result, message = check_guess(60, 50)
    assert result == "Too High"
    assert message == "📉 Go LOWER!"


def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    result, message = check_guess(40, 50)
    assert result == "Too Low"
    assert message == "📈 Go HIGHER!"


def test_check_guess_accepts_numeric_strings():
    result, message = check_guess("25", "30")
    assert result == "Too Low"
    assert message == "📈 Go HIGHER!"


@pytest.mark.parametrize(
    ("current_score", "outcome", "attempt_number", "expected_score"),
    [
        (0, "Win", 1, 100),
        (0, "Win", 4, 70),
        (5, "Win", 20, 15),
        (20, "Too High", 2, 15),
        (20, "Too Low", 2, 15),
        (20, "Unknown", 2, 20),
    ],
)
def test_update_score(current_score, outcome, attempt_number, expected_score):
    assert update_score(current_score, outcome, attempt_number) == expected_score
