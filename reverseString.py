# This function takes a string s as input and
# uses slicing to return the reverse of the string.
# The[::-1] syntax is a slice that starts from the end of the string(-1) and
# goes all the way to the beginning(-len(s)-1) in reverse order.
# This effectively reverses the string.
def reverse_string(s):
    return s[::-1]


s = input("Enter a string..")
reversed_s = reverse_string(s)
print(reversed_s)
