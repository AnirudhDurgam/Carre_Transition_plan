"""
This script takes a users input and counts the no.of words

"""

# Option 1

# message = input("Enter the sentence or message: ")
# word_count = len(message.split())
# print(word_count)


# Option 2

message = input("Enter the sentence or message: ")
word_count = message.split()
for index, word in enumerate(word_count, start=1):
    print(f"{word}:{index}", end=' ')
