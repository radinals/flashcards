import csv

from cards import Card, Deck
from dataclasses import fields as dt_fields

def csv_lines(file: str):
    with open(file) as f:
        for line in csv.reader(f, delimiter=',', quotechar='"'):
            yield line

# TODO: better way of unpacking a line
# TODO: GET THE CSV FORMAT FROM THE FIRST LINE


def get_card_val(line: list):
    card = Card()
    val_count = len(line)
    if val_count < 2:
        raise ValueError

    if line[0]:
        card.question = line[0]
    else:
        raise Exception

    if line[1]:
        card.answer = line[1]
    else:
        raise Exception

    if val_count > 2:
        card.difficulty = line[2]

    if val_count > 3:
        card.type = line[3]

    return card


def gen_deck(file):
    cards = []
    for line in csv_lines(file):
        cards.append(get_card_val(line))
    return Deck(cards)


def list_dataclass(dt):
    return ( (v.name, getattr(dt, v.name)) for v in dt_fields(dt) )
