import unittest
from card import Card
from deck import Deck

class TestDeck(unittest.TestCase):
    
    def test_deck_basic_example(self):
        deck = Deck()

        self.assertEqual(deck.size(), 52)

        card_one = deck.draw()
        card_two = deck.draw()
        
        self.assertEqual(deck.size(), 50)

        deck.add_card(card_one)
        self.assertEqual(deck.size(), 51)

        deck.reset()
        self.assertEqual(deck.size(), 52)

    # Please add tests to verify your Deck class below.

if __name__ == '__main__':
    unittest.main()