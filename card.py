from enum import Enum, IntEnum


class Color(Enum):
    __order__ = 'BLACK RED'
    BLACK = 1
    RED = 2


class Suit(Enum):
    __order__ = 'SPADES HEARTS CLUBS DIAMONDS'
    SPADES = 0
    HEARTS = 1
    CLUBS = 2
    DIAMONDS = 3


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
        self.wins = 0
        self.draws = 0
        self.losses = 0
        self.total = 0

    def get_display(self):
        display = ""
        if isinstance(self.rank, Rank):
            match self.rank:
                case Rank.ACE:
                    display = "A"
                case Rank.JACK:
                    display = "J"
                case Rank.QUEEN:
                    display = "Q"
                case Rank.KING:
                    display = "K"
        else:
            display = str(self.value)
        if self.suit is None:
            display += "B" if self.color == Color.BLACK else "R"
        else:
            match self.suit:
                case Suit.SPADES:
                    display += "S"
                case Suit.HEARTS:
                    display += "H"
                case Suit.CLUBS:
                    display += "C"
                case Suit.DIAMONDS:
                    display += "D"
        display += f": {self.wins}, {self.draws}, {self.losses}"
        return display

    @classmethod
    def from_joker(cls, color: Color):
        card = cls(None, 0)
        card.color = color
        return card

    def get_outcome(self, other: Card):
        if self.suit == other.suit:
            if self.value > other.value:
                return 1
            elif self.value < other.value:
                return -1
        elif self.color == other.color:
            if self.value < other.value:
                return 1
            elif self.value > other.value:
                return -1
        elif self.suit is None:
            return -1
        elif other.suit is None:
            return 1
        elif (self.suit.value + 1) % 4 == other.suit.value:
            return 1
        elif (self.suit.value - 1) % 4 == other.suit.value:
            return -1
        return 0

    def record_outcome(self, other: Card):
        if self.suit == other.suit and self.color == other.color and self.rank == other.rank:
            return
        outcome = self.get_outcome(other)
        if outcome == 1:
            self.wins += 1
        elif outcome == -1:
            self.losses += 1
        else:
            self.draws += 1
        self.total += 1


DECK = []
for suit in Suit:
    card = Card(suit, rank = Rank.ACE)
    DECK.append(card)
    for i in range(2, 11):
        card = Card(suit, rank = i)
        DECK.append(card)
    for r in (Rank.JACK, Rank.QUEEN, Rank.KING):
        card = Card(suit, rank = r)
        DECK.append(card)
for color in Color:
    card = Card.from_joker(color)
    DECK.append(card)
