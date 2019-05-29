from collections import defaultdict

class Solution:
    def __init__(self):
        pass
    def check_anagrams(self, string1, string2):
        """returns True if the 2 given strings are anagrams

        Args: 
            string1: string
            string2: string
        Returns:
           Bool
        """
        if len(string1) != len(string2):
            return False
        # char_frequency is a dictionary that maps a character to its 
        # number of occurences

        char_frequency = defaultdict(int)
        for c in string1:
            char_frequency[c] += 1
        for c in string2:
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