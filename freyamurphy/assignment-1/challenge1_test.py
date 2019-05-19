import unittest

import challenge1

class testChallenge1(unittest.TestCase):

    def test_Examples(self):
        self.assertTrue(challenge1.isAnagram("listen", "silent"))
        self.assertTrue(challenge1.isAnagram("triangle", "integral"))
        self.assertFalse(challenge1.isAnagram("apple", "pabble"))

    def test_anagramOfItself(self):
        self.assertTrue(challenge1.isAnagram("word", "word"))

    def test_differentLength(self):
        self.assertFalse(challenge1.isAnagram("abcde", "abcdef"))

    def test_oneLetter(self):
        self.assertTrue(challenge1.isAnagram("a", "a"));
        self.assertFalse(challenge1.isAnagram("a", "b"));

    def test_emptyString(self):
        self.assertTrue(challenge1.isAnagram("", ""));

    # to check that a letter can't be check off of string2 twice
    def test_repeatedLetter(self):
        self.assertFalse(challenge1.isAnagram("listenl", "silentg"))

    def test_caseInsensitive(self):
        self.assertTrue(challenge1.isAnagram("listen", "SILENT"))
