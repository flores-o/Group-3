from collections import defaultdict

class Solution:
    def __init__(self):
        pass
    def check_anagrams(self, s1, s2):
        """returns True if the 2 given strings are anagrams

        Args: 
            s1: string
            s2: string
        Returns:
           Bool
        """
        if len(s1) != len(s2):
            return False
        # char_frequency is a dictionary that maps a character to its 
        # number of occurences
        # for every character in s1, we increase its frequency with 1
        # for every character in s2, we decrease its frequency with 1
        # we return true if the char_frequency only contains pair of 
        # form (character, 0)
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

#changed something