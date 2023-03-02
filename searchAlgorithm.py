# This implementation takes two arguments: arr, 
# which is the sorted list to be searched, and target,
# which is the element to be found. 
# The function uses a while loop to repeatedly divide the search interval in 
# half until the target element is found or the search interval is empty.

# The left and right variables keep track of the current search interval, and 
# the mid variable is calculated as the average of left and right. If the element at mid is equal 
# to the target, the function returns the index of mid. If the element at mid is less than the target, 
# the search interval is narrowed to the right of mid. If the element at mid is greater than the target,
# the search interval is narrowed to the left of mid.

# If the target element is not found in the list, the function returns -1.

def binary_search(arr, target):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1


arr = [1, 3, 5, 7, 9]
target = 5
result = binary_search(arr, target)
print(result)  # prints 2
