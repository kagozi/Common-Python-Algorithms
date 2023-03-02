# This function takes a string s as input and uses slicing to compare 
# the original string with its reverse. If the reversed string is equal to the original string, 
# then the string is a palindrome and the function returns True. Otherwise, it returns False.



def is_palindrome(s):
    return s == s[::-1]
s = input("Enter a string...")

print(is_palindrome(s))