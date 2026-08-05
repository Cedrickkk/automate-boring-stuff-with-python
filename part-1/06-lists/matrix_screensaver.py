from random import random, randint, choice
import os, sys, time

NEW_DRIP_CHANCE: float = 0.02
DRIP_MIN_LENGTH: int = 4
DRIP_MAX_LENGTH: int = 14
FRAME_DELAY: float = 0.1
CHARACTERS: list[str] = ["0", "1"]

def get_terminal_width(fallback: int = 70) -> int:
    """Use the real terminal width"""
    try:
        return os.get_terminal_size().columns
    except OSError:
        return fallback

def make_next_row(drip_counters: list[int]) -> str:
    """Given the current drip counters, return the string for one printed row and update the counters in place for the next row"""
    characters_this_row: list[str] = []

    for i, remaining in enumerate(drip_counters):
        if remaining == 0 and random() < NEW_DRIP_CHANCE:
            drip_counters[i] = randint(DRIP_MAX_LENGTH, DRIP_MAX_LENGTH)

        if drip_counters[i] == 0:
            characters_this_row.append(" ")
        else:
            characters_this_row.append(choice(CHARACTERS))

    return "".join(characters_this_row)

def main() -> None:
    width = get_terminal_width()
    drip_counters = [0] * width

    try:
        while True:
            print(make_next_row(drip_counters))
            time.sleep(FRAME_DELAY)
    except KeyboardInterrupt:
        sys.exit()

if __name__ == "__main__":
    main()