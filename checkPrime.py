# Check if the number is less than 2. If it is, it cannot be a prime number and return False.
# Iterate through all numbers from 2 up to the square root of the number (inclusive) and check if the number is divisible by any of them. 
# If it is, it cannot be a prime number and return False.
# If the number is not divisible by any of the numbers in the range, it is a prime number and return True.
def is_prime(number):
    if number < 2:   # 0 and 1 are not prime numbers
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True


number = 17
if is_prime(number):
    print(f"{number} is a prime number")
else:
    print(f"{number} is not a prime number")