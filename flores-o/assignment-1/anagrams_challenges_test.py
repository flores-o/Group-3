import unittest
import string
from anagrams_challenges import Solution

class TestSolution(unittest.TestCase):
    def test_check_anagrams(self):
        self.assertTrue(Solution().check_anagrams('ana', 'naa'))
        self.assertTrue(Solution().check_anagrams('abcd', 'dbca'))
        self.assertFalse(Solution().check_anagrams('abcd', 'dbcc'))
    
    def test_check_case_insesitive(self):
        self.assertTrue(Solution().check_anagrams_case_insensitive('ANNA', 'Anan'))
        self.assertTrue(Solution().check_anagrams_case_insensitive('Abcccd', 'CCCDba'))
    
    def test_check_anagrams_sentences(self):
        self.assertTrue(Solution().check_anagrams_sentences(('Ana are ., m,ere'), ('A na, a reme re')))

    def test_check_anagrams_words_sentences(self):
        self.assertTrue(Solution().check_anagrams_words_sentences('Abc defg klm nopq', 'Acb fegd lmk npqo'))