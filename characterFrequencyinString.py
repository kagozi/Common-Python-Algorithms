# This function takes a string string as input and performs the following steps:

# Create an empty dictionary freq to store the frequency of each character in the string.
# Iterate through the string and update the frequency count for each character in freq.
# Return freq.

def count_chars_freq(string):
    freq = {}   # create an empty dictionary to store character frequencies
    for char in string:
        if char in freq:
            freq[char] += 1
        else:
            freq[char] = 1
    return freq


string = "abracadabra"
freq = count_chars_freq(string)
for char in freq:
    print(f"{char}: {freq[char]}")
