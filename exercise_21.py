"21. Write a Python program to find whether a given number (accept from the user) is even or odd, print out an appropriate message to the user."
def oddOrEven(n):
    """Tests if a number is odd or even and tells a user"""
    if n%2==0:
        return 'Even'
    else:
        return 'Odd'


x=int(input("Enter the integer you want to check: "))

print(oddOrEven(x))
