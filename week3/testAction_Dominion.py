from unittest import TestCase
import Dominion


# def __init__(self,name,cost,actions,cards,buys,coins):
# Card.__init__(self,name,"action",cost,0,0)
class actioncardTest(TestCase):
    def test___init__(self):
        #function that is used to verify that the init function values are equal
        ac = Dominion.Action_card("Randy", 4, 1, 0, 2, 3) #ac= action card
        self.assertEqual("Randy", ac.name)
        self.assertEqual(4, ac.cost)
        self.assertEqual(1, ac.actions)
        self.assertEqual(0, ac.cards)
        self.assertEqual(2, ac.buys)
        self.assertEqual(3, ac.coins)

    def test_use(self):
        #test function that verifiy if the card was played correctly
        player = Dominion.Player("Annie")
        player.hand = [Dominion.Moat()] * 1
        trash = []
        player.hand[0].use(player, trash)
        self.assertEqual(len(player.hand), 0)
        self.assertEqual(len(player.played), 1)

    def test_augment(self):
        #test function that we verify the data passed into the augment function
        player = Dominion.Player("Annie")
        card = Dominion.Action_card("Randy", 4, 1, 0, 2, 3)
        player.actions = 1
        player.purse = 1
        player.buys = 1
        card.augment(player)
        self.assertEqual(2, player.actions)
        self.assertEqual(4, player.purse)
        self.assertEqual(3, player.buys)
        self.assertEqual(5, len(player.hand))

