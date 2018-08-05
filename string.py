"""Finding the common substring."""


def sub_string(x, y):
    """Finding common substring"""
    x = set(list(x))
    y = set(list(y))
    if x in y:
        return "YES"
    else:
        return "NO"

n = int(input("Enter the number "))
for index in range(n):
    input1 = input("Enter the first string ")
    input2 = input("Enter the second string ")
    print(sub_string(input1, input2))
