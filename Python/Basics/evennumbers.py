number = int(input("Enter a number: "))
print(f"Even numbers from 1 to {number} are:")
for i in range(1, number + 1):
    if i % 2 == 0:  # if i %2 != 0: for odd numbers
        print(i)
