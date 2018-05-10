from unittest import TestCase
from game import game


class TestGame(TestCase):
    def test_isRepeat(self):
        g = game()
        self.assertEqual(g.isRepeat([0, 0]), False)

        g.player1.position = [[1, 2]]
        self.assertEqual(g.isRepeat([1, 2]), True)
        self.assertEqual(g.isRepeat([1, 3]), False)

        g.side = 1
        g.player2.position = [[2, 1]]

        self.assertEqual(g.isRepeat([1, 2]), True)
        self.assertEqual(g.isRepeat([1, 3]), False)
        self.assertEqual(g.isRepeat([2, 1]), True)

        del g

    def test_check(self):
        g = game()

        g.check()
        self.assertEqual(g.end, False)

        g.put_times = 9
        g.check()
        self.assertEqual(g.end, True)

        g.player1.position = [[0, 0], [0, 1], [0, 2]]
        g.check()
        self.assertEqual(g.end, True)
        del g

    def test_isWin(self):
        g = game()

        self.assertEqual(g.isWin([[0, 0], [0, 1], [1, 2]]),False)
        self.assertEqual(g.isWin([[0, 0], [0, 1], [0, 2]]),True)



    def test_draw(self):
        pass
        """
        #because is working,so hiding
        
        g = game()
        g.draw()

        g.player1.position=[[1,0],[1,1],[1,2]]
        g.player2.position=[[0,0],[0,1],[0,2]]
        g.draw()
        """
