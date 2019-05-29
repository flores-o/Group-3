# python -m unittest anagrams_test.py
import unittest
from anagrams import Solution

class TestSolution(unittest.TestCase):
    def test_check_anagrams1(self):
        self.assertTrue(Solution().check_anagrams('ana', 'naa'))
        self.assertTrue(Solution().check_anagrams('abcd', 'dbca'))
    def test_check_anagrams2(self):
        self.assertFalse(Solution().check_anagrams('abcd', 'dbcc'))