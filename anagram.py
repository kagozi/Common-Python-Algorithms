# This function takes two strings str1 and str2 as input and performs the following steps:

# Check if the lengths of the strings are different. If they are, they cannot be anagrams and return False.
# Create an empty dictionary count to store the count of each character in str1.
# Iterate through str1 and update the count for each character in count.
# Iterate through str2 and check if each character is in count. If it is , decrement its count in count. If it is not, or its count in count is already 0, it cannot be an anagram and return False.
# If all characters in str2 are in count and their counts are all greater than 0, the two strings are anagrams and return True.

def check_anagrams(str1, str2):
    if len(str1) != len(str2):   # check if lengths of strings are different
        return False
    count = {}   # create an empty dictionary to store character counts
    for char in str1:
        if char in count:
            count[char] += 1
        else:
            count[char] = 1
    for char in str2:
        if char not in count or count[char] == 0:
            return False
        count[char] -= 1
    return True


str1 = "silent"
str2 = "listen"
if check_anagrams(str1, str2):
    print(f"{str1} and {str2} are anagrams")
else:
    print(f"{str1} and {str2} are not anagrams")
