import sys

from deck import Deck
from card import Card

sys.tracebacklimit = 0

HAND_LIMIT = 21
EMPTY_HAND_ERR = "Cannot 'hit' on an empty hand!"
EMPTY_DECK_ERR = "Not enough cards left in the deck! Re-shuffle."
CARD_VALUES = {"Ace": 11, "Two": 2, "Three": 3, "Four": 4, "Five": 5, "Six": 6,
               "Seven": 7, "Eight": 8, "Nine": 9, "Ten": 10, "Jack": 10, "Queen": 10, "King": 10}


class Blackjack:
    # Creates a Blackjack game with a new Deck.
    def __init__(self):
        self.__deck = Deck()
        self.__current_hand = []
        self.__discard_pile = []

    # Computes the score of a hand.
    # For examples of hands and scores as a number.
    # 2,5 -> 7
    # 3, 10 -> 13
    # 5, King -> 15
    # 10, Ace -> 21
    # 10, 8, 4 -> Bust so return -1
    # 9, Jack, Ace -> 20
    # If the Hand is a bust return -1 (because it always loses)
    def _get_score(self, hand: list[Card]) -> int:
        ace = 0
        score = 0
        for card in hand:
            _card = str(card).split(' ')
            value = _card[0]
            score += CARD_VALUES[value]

            if value == "Ace":
                ace += 1

        # look for ace if over 21
        while ace and score > HAND_LIMIT:
            score -= 10
            ace -= 1

        return score

    # Prints the current hand and score.
    # E.g. would print out (Ace of Clubs, Jack of Spades, 21)
    # E.g. (Jack of Clubs, 5 of Diamonds, 8 of Hearts, "Bust!")
    def _print_current_hand(self):
        for card in self.__current_hand:
            print(f"{str(card)}, ", end='')

        print(self._get_score(self.__current_hand))

    # The previous hand put in discard pile and NOT shuffled back into the deck.
    # Should remove the top 2 cards from the current deck and
    # Set those 2 cards as the "current hand".
    # It should also print the current hand and score of that hand.
    # If less than 2 cards are in the deck,
    # then print an error instructing the client to shuffle the deck.
    def deal_new_hand(self):
        if self.__deck.size() < 2:
            raise Exception(EMPTY_DECK_ERR)

        if self.__current_hand:
            self._clear_hand()

        for _ in range(2):
            self.__current_hand.append(self.__deck.draw())
        self._print_current_hand()
        

    # Deals one more card to the current hand and prints the hand and score.
    # If no cards remain in the deck, print an error.
    def hit(self):
        if not self.__current_hand:
            raise Exception(EMPTY_HAND_ERR)

        new_card = self.__deck.draw()
        if new_card:
            self.__current_hand.append(new_card)
            self._print_current_hand()
            if self._get_score(self.__current_hand) >= HAND_LIMIT:
                self._clear_hand()
        else:
            raise Exception(EMPTY_DECK_ERR)

    # Reshuffles all cards in the "current hand" and "discard pile"
    # and shuffles everything back into the Deck.
    def reshuffle(self):
        self._clear_hand()
        self.__discard_pile.clear()
        self.__deck.reset()

    # Place current hand into discard pile.
    def _clear_hand(self):
        self.__discard_pile += self.__current_hand[:]
        self.__current_hand.clear()
