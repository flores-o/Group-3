from collections import defaultdict
import string
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

    def check_anagrams_case_insensitive(self, string1, string2):
        """returns True if the 2 given strings are case sensitive or 
        case insensitive anagrams 

        Args: 
            string1: string
            string2: string
        Returns:
           Bool
        """
        return self.check_anagrams(string1.lower(), string2.lower())
    
    def check_anagrams_sentences(self, string1, string2):
        """returns True if the 2 given strings are anagrams 
        of sentences, where the order of the letters is not tied 
        to words and punctuation and white characters are ignored

        Args: 
            string1: string
            string2: string
        Returns:
           Bool
        """
        exclude = set(string.punctuation + ' ')
        string1_new = ''.join(c for c in string1 if c not in exclude)
        string2_new = ''. join(c for c in string2 if c not in exclude)

        return self.check_anagrams(string1_new, string2_new)


    def check_anagrams_corresponding_words_sentences(self, string1, string2):
        """returns True if the 2 given strings are anagrams of sentences, 
        where each word in the first sentence is an anagram of the corresponding
        word in the second sentence

        Args: 
            string1: string
            string2: string
        Returns:
           Bool
        """
        string1_list = string1.split()
        string2_list = string2.split()

        if len(string1_list) != len(string2_list):
            return False

        for idx, elem_string1_list in enumerate(string1_list):
            if not self.check_anagrams(elem_string1_list, string2_list[idx]):
                return False
        return True


"""
if __name__ == '__main__':
    s = Solution()
    print(s.check_anagrams('ana', 'naa'))
    print(s.check_anagrams('abc', 'bbc'))
"""

#changed something