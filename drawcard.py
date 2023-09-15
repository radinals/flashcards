from dialog import Dialog

from enum import Enum

from cards import Card
from utils import list_dataclass

from dataclasses import dataclass, asdict


class PromptReturn(Enum):
    CORRECT = 1
    INCORRECT = 2
    SKIP = 3
    EXIT = 4


@dataclass
class DialogReturns():
    no_button = "cancel"
    yes_button = "ok"
    help_button = "help"
    extra_button = "extra"


class ReturnCode(Enum):
    terminate = -1
    correct_answer = 1
    incorrect_answer = 0
    skipped_card = 2


@dataclass
class DialogConfig:

    yes_label: str = None
    no_label: str = None

    help_button: bool = False
    help_label: str = None

    extra_button: bool = False
    extra_label: str = None

    def dict(self):
        conf = {}
        for k, v in asdict(self).items():
            if v:
                conf[str(k)] = v
        return conf


class DialogMenu:
    def __init__(self):
        self.width, self.height = 0, 0

    def yesno(self, message, config: DialogConfig):
        return Dialog().yesno(message, self.width, self.height, **config.dict())


class DrawCard():
    def __init__(self, card: Card):
        self.card = card

    def flip_dialog(self):

        d1_config = DialogConfig()
        d1_config.help_button = True
        d1_config.help_label = "Exit"
        d1_config.yes_label = "Flip"
        d1_config.no_label = "Skip"

        d2_config = DialogConfig()
        d2_config.help_button = True
        d2_config.extra_button = True
        d2_config.help_label = "Exit"
        d2_config.extra_label = "Flip"
        d2_config.yes_label = "Correct"
        d2_config.no_label = "Incorrect"

        c_question = self.card.question
        c_answer = self.card.question
        DR = DialogReturns()

        while (True):

            d1 = DialogMenu().yesno(c_question, d1_config)

            if d1 == DR.yes_button:
                # flip card (show the answer)
                d2 = DialogMenu().yesno(f"{c_question}: {c_answer}", d2_config)
                if d2 == DR.yes_button:
                    return ReturnCode.correct_answer
                elif d2 == DR.no_button:
                    return ReturnCode.incorrect_answer
                elif d2 == DR.extra_button:
                    continue

            elif d1 == DR.help_button:
                return ReturnCode.terminate

            elif d1 == DR.no_button:
                return ReturnCode.skipped_card
