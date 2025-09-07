import math
n = int(input("Enter a number: "))
result = result2 = 1
counter = n
# Using while loop
while counter > 0:
    result2 = result2*counter
    counter -= 1
print(f"The factorial of {n} using While loop is {result2}")


# Using for loop
for i in range(1, n + 1):
    result = result*i
print(f"The factorial of {n} using For loop is {result}")


# Using recursion

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)


print(f"The factorial of {n} using recursion function is {factorial(n)}")


# Using math module
result3 = math.factorial(n)
print(f"The factorial of {n} using math module is {result}")
