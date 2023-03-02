# This function takes a string s as input and performs the following steps:
# Split the string into a list of words using the split() method.
# Use a list comprehension to reverse each word in the list.
# Join the reversed words back into a string using the join() method, with a space between each word.

def reverse_words(s):
    words = s.split()   # split the string into words
    reversed_words = [word[::-1] for word in words]  # reverse each word
    return ' '.join(reversed_words)  # join the reversed words with spaces


s = input("Enter a string...")
print(reverse_words(s))