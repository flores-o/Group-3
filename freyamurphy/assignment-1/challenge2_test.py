import unittest

import challenge2

class testAnagrams(unittest.TestCase):

    def test_Examples(self):
        self.assertTrue(challenge2.isAnagram("listen", "silent"))
        self.assertTrue(challenge2.isAnagram("triangle", "integral"))
        self.assertFalse(challenge2.isAnagram("apple", "pabble"))

    def test_anagramOfItself(self):
        self.assertTrue(challenge2.isAnagram("word", "word"))

    def test_differentLength(self):
        self.assertFalse(challenge2.isAnagram("abcde", "abcdef"))

    def test_oneLetter(self):
        self.assertTrue(challenge2.isAnagram("a", "a"));
        self.assertFalse(challenge2.isAnagram("a", "b"));

    def test_emptyString(self):
        self.assertTrue(challenge2.isAnagram("", ""));

    # to check that a letter can't be checked off of string2 twice
    def test_repeatedLetter(self):
        self.assertFalse(challenge2.isAnagram("listenl", "silentg"))

    def test_caseInsensitive(self):
        self.assertTrue(challenge2.isAnagram("listen", "LISTEN"))

    # New tests for challenge2
    def test_ignoreSpace(self):
        self.assertTrue(challenge2.isAnagram("hello there", "hellothere"))

    def test_ignorePunctuation(self):
        self.assertTrue(challenge2.isAnagram("hello.", "elloh"))

    def test_fullSentence(self):
        self.assertTrue(challenge2.isAnagram("This, is a full:  sentence!", "Tiafec nes; hisllu tesn."))
