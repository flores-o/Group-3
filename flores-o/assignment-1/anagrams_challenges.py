from collections import defaultdict
import string
class Solution:
    def __init__(self):
        pass
    def check_anagrams(self, s1, s2):

        if len(s1) != len(s2):
            return False

        char_frequency = defaultdict(int)
        for c in s1:
            char_frequency[c] += 1
        for c in s2:
            char_frequency[c] -= 1
            if char_frequency[c] < 0:
                return False
        for c,freq in char_frequency.items():
            if freq != 0:
                return False
        return True

    def check_anagrams_case_insensitive(self, s1, s2):
        return self.check_anagrams(s1.lower(), s2.lower())
    
    def check_anagrams_sentences(self, s1, s2):
        exclude = set(string.punctuation + ' ')
        s1_new = ''.join(c for c in s1 if c not in exclude)
        s2_new = ''. join(c for c in s2 if c not in exclude)

        return self.check_anagrams(s1_new, s2_new)


    def check_anagrams_words_sentences(self, s1, s2):

        s1_list = s1.split()
        s2_list = s1.split()

        if len(s1_list) != len(s2_list):
            return False

        for idx in range(len(s1_list)):
            if self.check_anagrams(s1_list[idx], s2_list[idx]) == False:
                return False
        return True


"""
if __name__ == '__main__':
    s = Solution()
    print(s.check_anagrams('ana', 'naa'))
    print(s.check_anagrams('abc', 'bbc'))
"""

#changed something