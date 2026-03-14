def get_range_for_difficulty(difficulty: str):
    """Return (low, high) inclusive range for a given difficulty."""
    if difficulty == "Easy":
        return 1, 20
    if difficulty == "Normal":
        return 1, 100
    if difficulty == "Hard":
        return 1, 50
    return 1, 100


def parse_guess(raw: str):
    """
    Parse user input into an int guess.

    Returns: (ok: bool, guess_int: int | None, error_message: str | None)
    """
    if raw is None:
        return False, None, "Enter a guess."

    if raw == "":
        return False, None, "Enter a guess."

    try:
        if "." in raw:
            value = int(float(raw))
        else:
            value = int(raw)
    except Exception:
        return False, None, "That is not a number."

    return True, value, None


def check_guess(guess, secret):
    """
    Compare guess to secret and return (outcome, message).

    outcome examples: "Win", "Too High", "Too Low"
    """
    if guess == secret:
        return "Win", "🎉 Correct!"

    try:
        if guess > secret:
            return "Too High", "📉 Go LOWER!"
        else:
            return "Too Low", "📈 Go HIGHER!"
    except TypeError:
        g = str(guess)
        if g == secret:
            return "Win", "🎉 Correct!"
        if g > secret:
            return "Too High", "📉 Go LOWER!"
        return "Too Low", "📈 Go HIGHER!"


def update_score(current_score: int, outcome: str, attempt_number: int):
    """Update score based on outcome and attempt number."""
    if outcome == "Win":
        points = 100 - 10 * attempt_number
        if points < 10:
            points = 10
        return current_score + points

    if outcome == "Too High":
        return current_score - 5

    if outcome == "Too Low":
        return current_score - 5

    return current_score


if __name__ == "__main__":
    # get_range_for_difficulty
    assert get_range_for_difficulty("Easy") == (1, 20)
    assert get_range_for_difficulty("Normal") == (1, 100)
    assert get_range_for_difficulty("Hard") == (1, 50)

    # parse_guess
    assert parse_guess("") == (False, None, "Enter a guess.")
    assert parse_guess(None) == (False, None, "Enter a guess.")
    assert parse_guess("abc") == (False, None, "That is not a number.")
    assert parse_guess("42") == (True, 42, None)
    assert parse_guess("3.7") == (True, 3, None)

    # check_guess
    assert check_guess(50, 50)[0] == "Win"
    assert check_guess(60, 50)[0] == "Too High"
    assert check_guess(40, 50)[0] == "Too Low"

    # update_score
    assert update_score(0, "Win", 1) == 90
    assert update_score(0, "Win", 9) == 10
    assert update_score(100, "Too High", 1) == 95
    assert update_score(100, "Too Low", 1) == 95

    print("All assertions passed.")
