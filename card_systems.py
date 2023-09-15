
from cards import Deck, Card
from drawcard import DrawCard, ReturnCode

class LetnerSystem:
    def __init__(self, deck: Deck, box_amount=4):
        self.boxes = self.__empty_decks(box_amount)
        self.number_of_cards: int = len(deck.cards)
        self.box_amount: int = box_amount
        self.boxes[0] = deck

    @staticmethod
    def __empty_decks(n):
        return [Deck([]) for _ in range(n)]

    def __last_box_is_full(self):
        if self.boxes[-1].card_amount() >= self.number_of_cards:
            return True
        return False

    def run(self):
        run = True
        while (run):

            # modifying a copy of the boxes because
            # it is less error prone than modifying
            # the boxes directly.

            tmp_boxes = self.__empty_decks(self.box_amount)

            for box_i, box in enumerate(self.boxes):
                if box.card_amount() < 1:
                    continue
                for card in box.cards:
                    answer = DrawCard(card).flip_dialog()

                    # if correct append to next box
                    if answer == ReturnCode.correct_answer:
                        # 1 as long box_i+1 <= box_amount-1, 0 otherwise.
                        mod = int(box_i+1 < self.box_amount)
                        tmp_boxes[box_i+mod].add(card)

                    # if incorrect append to first box
                    # move the cards to the end of the list
                    elif answer in [ReturnCode.skipped_card, ReturnCode.incorrect_answer, None]:
                        tmp_boxes[0].add(card)

                    elif answer == ReturnCode.terminate:
                        run = False
                        break

            # modifying/updating the boxes with the modified copy
            self.boxes = tmp_boxes
            del tmp_boxes

            # check if the last box has all of the cards or more
            if self.__last_box_is_full():
                run = False
