import unittest
from animals import Animal, Fish, Shark

class TestMoves(unittest.TestCase):

    # def test_random_move(self):
    #     a_test = Animal([1, 1])
    #     inv = [[0,1], [1,0],[-1, 0], [0,-1]]
    #     inv2 = [[1,0],[-1, 0], [0,-1]]
    #     inv3 = [[-1, 0], [0,-1]]
    #     inv4 = [[0,-1]]
    #     inv5 = []
    #     self.assertEqual(a_test._random_move(inv), None)
    #     self.assertEqual(a_test._random_move(inv2), [0,1])
    #     self.assertIn(a_test._random_move(inv3), [[1,0], [0,1]])
    #     self.assertIn(a_test._random_move(inv4), [[1,0], [0,1], [-1, 0],])
    #     self.assertIn(a_test._random_move(inv5), [[0,1], [1,0],[-1, 0], [0,-1]])

    def test_fish_move(self):
        f_test = Fish([1, 1])
        # surrounding = [[0,1], [1,0],[-1, 0], [0,-1]]
        self.assertEqual(f_test.move([[0,1], [1,0], [-1, 0]]), [1, 2])
        self.assertEqual(f_test.move([[0,1], [1,0], [-1, 0], [0,-1]]), None)
        self.assertIn(f_test.move([[-1, 0], [0,-1]]), [[1, 0], [0, 1]])
        self.assertIn(f_test.move([[-1, 0]]), [[1, 0], [0, 1], [1, 2]])
        self.assertIn(f_test.move([]), [[1, 0], [0, 1], [1, 2], [2, 1]])

    def test_shark_move(self):
        s_test = Fish([1, 1])
        # surrounding = [[0,1], [1,0],[-1, 0], [0,-1]]
        self.assertEqual(s_test.move([[0,1], [1,0], [-1, 0]]), [1, 2])
        self.assertEqual(s_test.move([[0,1], [1,0], [-1, 0], [0,-1]]), None)
        self.assertIn(s_test.move([[-1, 0], [0,-1]]), [[1, 0], [0, 1]])
        self.assertIn(s_test.move([[-1, 0]]), [[1, 0], [0, 1], [1, 2]])
        self.assertIn(s_test.move([]), [[1, 0], [0, 1], [1, 2], [2, 1]])


    # def test_shark_moveto_fish(self):
    #     s_test = Shark([1, 1])
    #     f = []
    #     self.assertEqual(s_test.move_to_fish(f), None)
    #     # surrounding = [[0,1],[1,0],[1,2],[2,1]]
    #     f1 = [[0,1],[1,0],[1,2],[2,1]]
    #     self.assertIn(s_test.move_to_fish(f1), [[0,1],[1,0],[1,2],[2,1]])
    #     f2 = [[0,1],[1,0],[1,2]]
    #     self.assertIn(s_test.move_to_fish(f2), [[0,1],[1,0],[1,2]])
    #     f3 = [[1,2],[2,1]]
    #     self.assertIn(s_test.move_to_fish(f3), [[1,2],[2,1]])
    #     f4 = [[2,1]]
    #     self.assertIn(s_test.move_to_fish(f4), [[2,1]])



if __name__ == '__main__':
    unittest.main()
