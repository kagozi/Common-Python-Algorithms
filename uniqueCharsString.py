# Check if the length of the string is greater than 128. If it is , the string must contain duplicate characters and return False.
# Create an array char_set of length 128 (the number of unique ASCII characters) initialized to False.
# Iterate through the string and check if each character has been seen before by looking 
# up its ASCII code in char_set. If it has, 
# the string contains duplicate characters and return False.
# If all characters are unique, return True.
def has_unique_chars(string):
    if len(string) > 128:   # no string can have more than 128 unique ASCII characters
        return False
    # create an array to store whether each character has been seen
    char_set = [False] * 128
    for char in string:
        if char_set[ord(char)]:
            return False
        char_set[ord(char)] = True
    return True


string1 = "abcdefg"
if has_unique_chars(string1):
    print(f"{string1} has all unique characters")
else:
    print(f"{string1} does not have all unique characters")

string2 = "abcdeff"
if has_unique_chars(string2):
    print(f"{string2} has all unique characters")
else:
    print(f"{string2} does not have all unique characters")
