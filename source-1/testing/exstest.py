import unittest
import exs

class TestGame(unittest.TestCase):
    # def test_input(self):
    #     answer = 5
    #     guess = 5
    #     result = exs.run_guess(guess, answer)
    #     self.assertTrue(result)

    def test_input(self):
        result = exs.run_guess(5, 5)
        self.assertTrue(result)

    def test_wrong_guess(self):
        result = exs.run_guess(5, 0)
        self.assertFalse(result)

    def test_wrong_number(self):
        result = exs.run_guess(5, 11)
        self.assertFalse(result)

    def test_wrong_type(self):
        result = exs.run_guess(5, '11')
        self.assertFalse(result)

    if __name__ == '__main__':
        unittest.main()