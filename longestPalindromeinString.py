# Initialize an empty string longest_palindrome to store the longest palindrome found.
# Iterate through all possible substrings of string, i.e., all pairs of indices(i, j) with i <= j.
# Check if the substring string[i:j] is a palindrome by comparing it to its reverse using string[i:j][::-1].
# If the substring is a palindrome and its length is greater than the length of longest_palindrome, update longest_palindrome to the substring.
# Return longest_palindrome.
def largest_palindrome(string):
    longest_palindrome = ""
    for i in range(len(string)):
        for j in range(i+1, len(string)+1):
            substring = string[i:j]
            if substring == substring[::-1] and len(substring) > len(longest_palindrome):
                longest_palindrome = substring
    return longest_palindrome

string = "forgeeksskeegfor"
longest_palindrome = largest_palindrome(string)
print(f"The longest palindrome in {string} is {longest_palindrome}")
