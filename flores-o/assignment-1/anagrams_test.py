import unittest
from anagrams import Solution

class TestSolution(unittest.TestCase):
    def test_check_anagrams(self):
        self.assertTrue(Solution().check_anagrams('ana', 'naa'))
        self.assertTrue(Solution().check_anagrams('abcd', 'dbca'))
        self.assertFalse(Solution().check_anagrams('abcd', 'dbcc'))