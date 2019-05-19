# This is the first assignment of Dongqing Wang
def areAnagram(str1, str2):
    '''
    Given two strings, determine if one is an anagram of the other.
    Two words are anagrams of each other if they are made of the same letters
    in a different order.

    **Case sensitive

    For example:
    - "listen" and "silent" are anagrams
    - "triangle" and "integral" are anagrams
    -  "apple" and "pabble" are NOT anagrams
    '''
    str1_len = len(str1)
    str2_len = len(str2)

    if str1_len != str2_len:
        return False

    str1_sorted = sorted(str1)
    str2_sorted = sorted(str2)

    for x in range(str1_len):
        if str1_sorted[x] != str2_sorted[x]:
            return False

    return True
