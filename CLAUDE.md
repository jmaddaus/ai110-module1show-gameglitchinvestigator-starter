# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

AI110 Module 1 assignment: a deliberately buggy Streamlit number-guessing game. Students find and fix intentional bugs, then refactor logic into a utility module and pass tests.

## Commands

- **Run the app:** `python -m streamlit run app.py`
- **Run tests:** `pytest`
- **Install dependencies:** `pip install -r requirements.txt` (uses `.venv/` virtual environment)

## Architecture

- **app.py** — Streamlit UI and game loop. Contains inline game logic functions (`get_range_for_difficulty`, `parse_guess`, `check_guess`, `update_score`) that are intentionally buggy and need to be refactored into `logic_utils.py`.
- **logic_utils.py** — Stub module with `NotImplementedError` placeholders. Students move corrected logic here; `app.py` should then import from this module.
- **tests/test_game_logic.py** — Pytest tests that import `check_guess` from `logic_utils`. Tests expect `check_guess` to return just the outcome string (`"Win"`, `"Too High"`, `"Too Low"`), not the tuple that `app.py` currently returns.

## Known Intentional Bugs (in app.py)

1. **Reversed hints** — `check_guess` says "Go HIGHER" when guess is too high, and vice versa.
2. **Type coercion bug** — On even attempts, the secret is cast to `str`, causing type-mismatch comparisons.
3. **Difficulty range wrong** — Hard mode range (1-50) is easier than Easy mode (1-20); these are swapped.
4. **Score calculation off-by-one** — `update_score` uses `attempt_number + 1` instead of `attempt_number` for win points.
5. **Inconsistent score penalties** — "Too High" alternates between +5 and -5 based on attempt parity.

## Key Detail for Tests

`test_game_logic.py` expects `check_guess(guess, secret)` to return a single string (the outcome), not a `(outcome, message)` tuple. The refactored `logic_utils.check_guess` must match this interface.
