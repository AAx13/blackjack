import random

from card import Card

DECK_MAX_SIZE = 52


class Deck:

    # Creates a sorted deck of playing cards. 13 values, 4 suits.
    # You will iterate over all pairs of suits and values to add them to the deck.
    # Once the deck is initialized, you should prepare it by shuffling it once.
    def __init__(self):
        SUITS = ["Diamonds", "Spades", "Hearts", "Clubs"]
        VALUES = ["Ace", "Two", "Three", "Four", "Five", "Six",
                  "Seven", "Eight", "Nine", "Ten", "Jack", "Queen", "King"]

        self.__deck = []
        for s in range(len(SUITS)):
            for v in range(len(VALUES)):
                self.__deck.append(
                    Card(SUITS[s], VALUES[v]))
        self.shuffle()

    # Returns the number of Cards in the Deck
    def size(self):
        return len(self.__deck)

    # Shuffles the deck of cards. This means randomzing the order of the cards in the Deck.
    def shuffle(self):
        random.shuffle(self.__deck)

    # Returns the top Card in the deck, but does not modify the deck.
    def peek(self):
        return self.__deck[-1]

    # Removes and returns the top card in the deck. The card should no longer be in the Deck.
    def draw(self):
        try:
            top = self.__deck[-1]
            self.__deck.pop()
            return top
        except:
            print("Deck is empty!")

    # Adds the input card to the deck.
    # If the deck has more than 52 cards, do not add the card and raise an exception.
    def add_card(self, card):
        if len(self.__deck) < DECK_MAX_SIZE:
            self.__deck.append(card)
        else:
            raise Exception("Deck is full!")

    # Calling this function should print all the cards in the deck in their current order.
    def print_deck(self):
        print([str(card) for card in self.__deck])

    # Resets the deck to it's original state with all 52 cards.
    # Also shuffle the deck.
    def reset(self):
        self.__init__()
