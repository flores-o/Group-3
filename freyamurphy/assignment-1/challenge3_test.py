import unittest

import challenge3

class testAnagrams(unittest.TestCase):

    def test_Examples(self):
        self.assertTrue(challenge3.isAnagram("listen", "silent"))
        self.assertTrue(challenge3.isAnagram("triangle", "integral"))
        self.assertFalse(challenge3.isAnagram("apple", "pabble"))

    def test_anagramOfItself(self):
        self.assertTrue(challenge3.isAnagram("word", "word"))

    def test_differentLength(self):
        self.assertFalse(challenge3.isAnagram("abcde", "abcdef"))

    def test_oneLetter(self):
        self.assertTrue(challenge3.isAnagram("a", "a"));
        self.assertFalse(challenge3.isAnagram("a", "b"));

    def test_emptyString(self):
        self.assertTrue(challenge3.isAnagram("", ""));

    # to check that a letter can't be checked off of string2 twice
    def test_repeatedLetter(self):
        self.assertFalse(challenge3.isAnagram("listenl", "silentg"))

    def test_caseInsensitive(self):
        self.assertTrue(challenge3.isAnagram("listen", "LISTEN"))

    def test_ignorePunctuation(self):
        self.assertTrue(challenge3.isAnagram("hello.", "elloh"))

    # New for challenge 3
    def test_twoWords(self):
        self.assertTrue(challenge3.sentenceIsAnagram("listen triangle", "silent integral"))

    def test_wordPositionMatches(self):
        self.assertFalse(challenge3.sentenceIsAnagram("listen triangle", "integral silent"))

    def test_oneWord(self):
        self.assertTrue(challenge3.sentenceIsAnagram("listen", "silent"))

    def test_twoConsecutiveSpaces(self):
        self.assertTrue(challenge3.sentenceIsAnagram("listen  triangle", "silent integral"))
