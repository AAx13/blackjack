import unittest
from card import Card
from deck import Deck
from blackjack import Blackjack

class TestBlackjack(unittest.TestCase):
    
    def test_blackjack_basic_example(self):
        blackjack = Blackjack()

        hand = [Card("Spades", "Ace"), Card("Spades", "Jack")]
        self.assertEqual(blackjack._get_score(hand), 21)

    # Please add significant tests to verify the Blackjack _get_score class 
    # You can ignore the additional Blackjack methods as they are randomized.

if __name__ == '__main__':
    unittest.main()