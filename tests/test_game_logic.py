from logic_utils import check_guess, get_range_for_difficulty, update_score


# --- check_guess: hints should point the player in the correct direction ---

def test_winning_guess():
    outcome, message = check_guess(50, 50)
    assert outcome == "Win"

def test_guess_too_high_gives_lower_hint():
    outcome, message = check_guess(60, 50)
    assert outcome == "Too High"
    assert "LOWER" in message

def test_guess_too_low_gives_higher_hint():
    outcome, message = check_guess(40, 50)
    assert outcome == "Too Low"
    assert "HIGHER" in message


# --- get_range_for_difficulty: harder = wider range ---

def test_easy_range_is_smallest():
    _, easy_high = get_range_for_difficulty("Easy")
    _, normal_high = get_range_for_difficulty("Normal")
    assert easy_high < normal_high

def test_hard_range_is_largest():
    _, normal_high = get_range_for_difficulty("Normal")
    _, hard_high = get_range_for_difficulty("Hard")
    assert hard_high > normal_high


# --- update_score: no parity-based penalty flip, correct win formula ---

def test_win_score_first_attempt():
    # 100 - 10 * 1 = 90
    assert update_score(0, "Win", 1) == 90

def test_win_score_fifth_attempt():
    # 100 - 10 * 5 = 50
    assert update_score(0, "Win", 5) == 50

def test_too_high_penalty_is_consistent():
    # Both even and odd attempts should give the same penalty
    score_even = update_score(100, "Too High", 2)
    score_odd = update_score(100, "Too High", 3)
    assert score_even == score_odd

def test_too_high_deducts_five():
    assert update_score(100, "Too High", 1) == 95

def test_too_low_deducts_five():
    assert update_score(100, "Too Low", 1) == 95
