# This function takes a list of integers nums as input and performs the following steps:

# Determine the total number of integers in the sequence, including the missing one, by adding 1 to the length of the input list.
# Calculate the expected sum of the integers in the sequence using the formula n * (n + 1) // 2, 
# where n is the total number of integers in the sequence.
# Calculate the actual sum of the integers in the input list using the sum() function.
# Calculate the missing number by subtracting the actual sum from the expected sum.

def find_missing_number(nums):
    # total number of integers in the sequence, including the missing one
    n = len(nums) + 1
    # expected sum of the integers in the sequence
    expected_sum = n * (n + 1) // 2
    actual_sum = sum(nums)   # actual sum of the integers in the list
    missing_number = expected_sum - actual_sum   # calculate the missing number
    return missing_number


nums = [1, 2, 3, 5, 6, 7, 8, 9, 10]
missing_number = find_missing_number(nums)
print(missing_number)
