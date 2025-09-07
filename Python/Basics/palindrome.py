name_ = input("Enter your string: ")
reversed_name = "".join(reversed(name_))
if name_ == reversed_name:
    print("The provided input is a valid Palindrome")
else:
    print("The provided input is not a Valid Palindrome")
