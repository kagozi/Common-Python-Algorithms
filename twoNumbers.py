# This function takes a list of integers nums and a target value target as input and performs 
# the following steps:
# Create an empty dictionary complements to store complements.
# Iterate through the list of numbers using the enumerate() function to access both the index and the value of each number.
# Calculate the complement of each number by subtracting it from the target value.
# Check if the complement is already in the dictionary complements. If it is, return a
# list containing the indices of the two numbers that add up to the target value.
# If the complement is not in the dictionary, store the current number's index as the value in the dictionary, with the current number as the key.
# If no two numbers add up to the target value, return None.

def find_two_numbers(nums, target):
    complements = {}   # dictionary to store complements
    for i, num in enumerate(nums):
        complement = target - num   # calculate complement
        if complement in complements:
            j = complements[complement]   # get index of complement
            return [j, i]   # return indices of two numbers
        # store index of current number as value in dictionary
        complements[num] = i
    return None   # return None if no two numbers add up to target


nums = [2, 7, 11, 15]
target = 9
result = find_two_numbers(nums, target)
print(result)  # [0, 1]

