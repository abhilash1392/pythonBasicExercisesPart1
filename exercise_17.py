"18. Write a Python program to calculate the sum of three given numbers, if the values are equal then return three times of their sum."

def sumOfThreeNumbers(x,y,z):
    """Returns the sum of three numbers if they are equal then
    return three times their sum

    Args:
        x ([int]): [First Number]
        y ([int]): [Second Number]
        z ([int]): [Third Number]
    """

    if x==y and y==z:
        return 3*(x+y+z)

    else:
        return x+y+z


x=int(input("Enter the First Number: "))
y=int(input("Enter the Second Number: "))
z=int(input("Enter the Third Number: "))

print(sumOfThreeNumbers(x,y,z))

