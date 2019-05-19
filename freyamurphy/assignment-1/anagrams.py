
import sys

def main():
    if len(sys.argv) != 3:
        print("Invalid input.")
        print("Usage: python anagrams.py string1 string2")
    else:
        string1 = sys.argv[1]
        string2 = sys.argv[2]
        result = isAnagram(string1, string2);
        print(result)

# Return True is string1 is an anagram of string 2, and False otherwise
def isAnagram(string1, string2):
    # Anagrams must be the same length
    if len(string1) != len(string2):
        return False

    # Check whether each letter in string1 is in string2
    for letter1 in string1:

        found = False
        letter2pos = 0
        while (not(found) and letter2pos < len(string2)):
            letter2 = string2[letter2pos]

            # The letter from string1 is in string2
            if letter1 == letter2:
                found = True
                # delete letter2 from string2
                string2 = string2[:letter2pos] + string2[letter2pos+1:]

            letter2pos += 1

        # The letter from string1 is not in string2
        if not(found):
            return False

    return True

#main()
