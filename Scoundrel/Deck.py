from collections import deque
from Scoundrel import settings as s
import random as rand


class Deck:

    __cards = None

    def __init__(self, deck_seed=None):
        cards = s.CARDS
        rand.seed(deck_seed)
        rand.shuffle(cards)
        self.__cards = deque(cards)

    def draw(self):
        if len(self.__cards) == 0:
            return False, 0
        return True, self.__cards.pop()

    def back(self, card):
        self.__cards.appendleft(card)

    def remaining(self):
        return len(self.__cards)

    def score(self):
        score = 0
        for c in self.__cards:
            if suit(c) in {0, 1}:
                score -= value(c)
        return score

    def __repr__(self):
        return "an enchanting deck of " + str(self.remaining()) + " cards."


# Cards Handling
def card2str(card):
    return "a " + str(value(card)) + " of " + s.CARDS_SUIT[suit(card)]


def suit(card):
    return int(card/13)


def value(card):
    return (card % 13)+2
