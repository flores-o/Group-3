from collections import defaultdict

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
"""
if __name__ == '__main__':
    s = Solution()
    print(s.check_anagrams('ana', 'naa'))
    print(s.check_anagrams('abc', 'bbc'))
"""