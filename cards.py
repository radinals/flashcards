import random

from dataclasses import dataclass

# NOTE
# deck is a 2d list
# [ ["question", "answer", "state"] ]


@dataclass()
class Card():
    question = None
    answer = None
    difficulty = -1
    card_type = "FLIP"


class Deck():
    def __init__(self, cards):
        self.cards = cards

    def swap_card(self, from_x: int, with_x: int):
        tmp = self.cards[with_x]
        self.cards[with_x] = self.cards[from_x]
        self.cards[from_x] = tmp

    def shuffle(self, num: int = 1):
        for _ in range(0, num):
            random.shuffle(self.cards)

    def add(self, card: Card):
        self.cards.append(card)

    def rmv(self, card: Card):
        self.cards.pop(self.cards.index(card))

    def card_amount(self):
        return len(self.cards)

    def change_card_type(self, card_index, new_type):
        self.cards[card_index].card_type = new_type
