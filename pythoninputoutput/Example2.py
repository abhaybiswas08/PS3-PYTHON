import sys

# print to sys.stdout.
print("Good Afternoon.", file=sys.stdout)

# print to a file named 'file.txt'.
with open('file.txt', 'w') as f:
    print("My Name is Abhay.", file=f)
