import unittest
from animals import Animal, Fish, Shark

class TestMoves(unittest.TestCase):

    def test_random_move(self):
        a_test = Animal([1, 1])
        inv = [[0,1], [1,0],[-1, 0], [0,-1]]
        inv2 = [[1,0],[-1, 0], [0,-1]]
        inv3 = [[-1, 0], [0,-1]]
        inv4 = [[0,-1]]
        inv5 = [[-1, 0], [0,-1]]
        self.assertEqual(a_test._random_move(inv), None)
        self.assertEqual(a_test._random_move(inv2), [0,1])
        self.assertIn(a_test._random_move(inv3), [[1,0], [0,1]])
        self.assertIn(a_test._random_move(inv4), [[1,0], [0,1], [-1, 0],])
        self.assertIn(a_test._random_move(inv5), [[0,1], [1,0],[-1, 0], [0,-1]])

    def shark_fish_move(self):
        s_test = Shark([1,1])
        f = []
        self.assertEqual(s_test.move_to_fish(f), None)

if __name__ == '__main__':
    unittest.main()
