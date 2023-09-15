#!/bin/python3

from utils import gen_deck
from card_systems import LetnerSystem

def main():
    # RULES:
    # NONE = SKIP
    # TRUE = CORRECT
    # FALSE = INCORRECT

    file = "test.csv"

    LetnerSystem(gen_deck(file)).run()


if __name__ == "__main__":
    main()
