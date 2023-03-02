# The FizzBuzz problem is a simple programming problem that requires printing out numbers from 1 to n, but with some modifications:

# For numbers that are multiples of 3, print "Fizz" instead of the number
# For numbers that are multiples of 5, print "Buzz" instead of the number
# For numbers that are multiples of both 3 and 5, print "FizzBuzz" instead of the number

def fizzbuzz(n):
    for i in range(1, n+1):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)
# fizzbuzz(5)
element = int(input("Enter a number..."))
fizzbuzz(element)
