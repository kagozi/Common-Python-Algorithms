# This function takes a list of numbers nums as input and performs the following steps:

# Check if the list is empty. If it is, return None for both the maximum and minimum elements.
# Initialize variables max_num and min_num to the first element of the list.
# Iterate through the list of numbers and compare each element to the current maximum and minimum.
# If the current element is greater than max_num, update max_num.
# If the current element is less than min_num, update min_num.
# Return the maximum and minimum elements.


def find_max_min(nums):
    if not nums:   # check if list is empty
        return None, None
    # initialize max_num and min_num to first element of list
    max_num, min_num = nums[0], nums[0]
    for num in nums:
        if num > max_num:
            max_num = num
        elif num < min_num:
            min_num = num
    return max_num, min_num


nums = [3, 5, 2, 8, 1, 7, 9]
max_num, min_num = find_max_min(nums)
print(f"Maximum: {max_num}, Minimum: {min_num}")   # Maximum: 9, Minimum: 1
