# pyint
# pyflake8

# PEP 8

import unittest
import main

class TestMain(unittest.TestCase):
    def test_do_stuff(self):
        test_param = 10
        result = main.do_stuff(test_param)
        self.assertEqual(result, 15)
        
    def test_do_stuff2(self):
        test_param = 'asdasdsa'
        result = main.do_stuff(test_param)
        # self.assertTrue(isinstance(result, ValueError))
        self.assertIsInstance(result, ValueError)
        
    
    def test_do_stuff3(self):
        test_param = None
        result = main.do_stuff(test_param)
        self.assertEqual(result, '_Please provide a valid number_')
        
    def test_do_stuff4(self):
        test_param = ''
        result = main.do_stuff(test_param)
        self.assertEqual(result, '_Please provide a valid number_')

if __name__ == '__main__':
    unittest.main()
# This code is a unit test for the do_stuff function in the main module.\
