"""16. Write a Python program to get the difference between a given number and 17, if the number is greater than 17 return double the absolute difference."""

def diff17():
    """Give the difference between the given number and 17 if the number is greater than 17 return double the absolute difference
    """

    x=int(input('Enter the number you want to subtract from 17: '))

    if x>17:
        return 2*(x-17)

    else:
        return x-17


print(diff17())