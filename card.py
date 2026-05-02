from enum import Enum, IntEnum


class Color(Enum):
    BLACK = 1
    RED = 2


class Suit(Enum):
    SPADES = 1
    HEARTS = 2
    CLUBS = 3
    DIAMONDS = 4


class Rank(Enum):
    ACE = 1
    JACK = 11
    QUEEN = 12
    KING = 13


class Card(object):
    def __init__(self, suit: Suit | None, rank: Rank | int):
        self.suit = suit
        self.color = Color.BLACK if self.suit in (Suit.SPADES, Suit.CLUBS) else Color.RED
        self.rank = rank
        self.value = 0
        if isinstance(self.rank, Rank):
            if self.rank == Rank.ACE:
                self.value = 1
            else:
                self.value = 11
        else:
            self.value = self.rank

    @classMethod
    def from_joker(cls, color: Color):
        card = cls(None, 0)
        card.color = color
        return card
