class Card:

    # Card constructor
    # The suit and value of a card, should be immutable.
    def __init__(self, suit, value):
        self._suit = suit
        self._value = value

    # Returns the suit of the card.
    def suit(self):
        return self._suit

    # Returns the value of the card.
    def value(self):
        return self._value

    # Returns a string representation of Card
    # E.g. "Ace of Spades"
    def __str__(self):
        return f"{self._value} of {self._suit}"
