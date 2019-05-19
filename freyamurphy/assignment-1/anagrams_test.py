import unittest

import anagrams

class testAnagrams(unittest.TestCase):

    def test_Examples(self):
        self.assertTrue(anagrams.isAnagram("listen", "silent"))
        self.assertTrue(anagrams.isAnagram("triangle", "integral"))
        self.assertFalse(anagrams.isAnagram("apple", "pabble"))

    def test_anagramOfItself(self):
        self.assertTrue(anagrams.isAnagram("word", "word"))

    def test_differentLength(self):
        self.assertFalse(anagrams.isAnagram("abcde", "abcdef"))

    def test_oneLetter(self):
        self.assertTrue(anagrams.isAnagram("a", "a"));
        self.assertFalse(anagrams.isAnagram("a", "b"));

    def test_emptyString(self):
        self.assertTrue(anagrams.isAnagram("", ""));

    # to check that a letter can't be check off of string2 twice
    def test_repeatedLetter(self):
        self.assertFalse(anagrams.isAnagram("listenl", "silentg"))

    def test_caseSensitive(self):
        self.assertFalse(anagrams.isAnagram("listen", "LISTEN"))
