from unittest import TestCase
import Dominion

class gameover(TestCase):
    def test_gameover(self):
        # test function that checks if the game has ended by creating a supply then popping values to check if it ends
        supply = {"Province": [Dominion.Province()] * 1,
                  "Duchy": [Dominion.Duchy()] * 2,
                  "Moat": [Dominion.Moat()] * 1,
                  "Thief": [Dominion.Thief()] * 1,
                  "Gold": [Dominion.Gold()] * 1}
       #pop the supply then check if the gameover function asserts true
        supply["Province"].pop(0)
        supply["Duchy"].pop(0)
        supply["Moat"].pop(0)
        supply["Thief"].pop(0)
        supply["Gold"].pop(0)
        self.assertTrue(Dominion.gameover(supply))