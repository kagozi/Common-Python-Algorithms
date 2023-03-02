# This function takes two sorted lists list1 and list2 as input and performs the following steps:

# Create an empty list merged_list to store the merged sorted list.
# Initialize two index variables i and j to 0 for both lists.
# Use a while loop to compare the elements at the current indices of both lists.
# Append the smaller element to merged_list and increment the index of the list it came from.
# Continue this process until one of the lists has been completely merged into merged_list.
# Add the remaining elements from the other list to merged_list.
# Return the merged sorted list.
def merge_sorted_lists(list1, list2):
    merged_list = []   # create an empty list to store the merged sorted list
    i, j = 0, 0   # initialize index variables for both lists
    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            merged_list.append(list1[i])
            i += 1
        else:
            merged_list.append(list2[j])
            j += 1
    # add remaining elements from both lists
    merged_list += list1[i:]
    merged_list += list2[j:]
    return merged_list


list1 = [1, 3, 5, 7]
list2 = [2, 4, 6, 8]
merged_list = merge_sorted_lists(list1, list2)
print(merged_list)  # [1, 2, 3, 4, 5, 6, 7, 8]
