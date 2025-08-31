"""
This script takes a users input and reverses 
"""
# Option 1

# actual_string = input("Enter your string: ")
# reversed_string = actual_string[::-1]
# print(reversed_string)


# Option 2

actual_string = input("Enter your string: ")
reversed_string = "".join(reversed(actual_string))
print(reversed_string)
