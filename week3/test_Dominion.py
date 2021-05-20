from unittest import TestCase
import Dominion

class testplayer(TestCase):
    #test function for action balance, create player then add a card to check the balance
    def test_action_balance(self):
        player = Dominion.Player("Annie")
        player.hand.append(Dominion.Moat())
        bal = player.action_balance()
        self.assertEqual(11, len(player.stack()))
        self.assertEqual(-6, int(bal))

    def test_calcpoints(self):
        # test function to calculate the points for the player
        player = Dominion.Player("Annie")
        player.deck.append(Dominion.Duchy())
        player.deck.append(Dominion.Gardens())
        pts = player.calcpoints()
        self.assertEqual(7, pts)

    def test_draw(self):
        # test function that checks if cards are added and discarded properly
        player = Dominion.Player("Annie")
        player.deck = [Dominion.Moat()] * 1
        player.hand = []
        player.discard = [Dominion.Gold()] * 4
        # draw moat that asserts its in the hand
        self.assertTrue(player.draw().name == "Moat")
        self.assertTrue(len(player.hand) > 0)
        self.assertTrue(player.hand[0].name == "Moat")
        # call draw function by name  "gold" then asserts if in the hand
        self.assertTrue(player.draw().name == "Gold")
        self.assertTrue(player.hand[1].name == "Gold")

    def test_cardsummary(self):
        # test function that verifies if its summarizes correctly
        player = Dominion.Player("Annie")
        player.deck.append(Dominion.Moat())
        cs = player.cardsummary() #cardsummary
        self.assertEqual(4, len(cs))
        self.assertEqual(1, cs["Moat"])
        self.assertEqual(3, cs["Estate"])
        self.assertEqual(3, cs["VICTORY POINTS"])

