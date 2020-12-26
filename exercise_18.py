"17. Write a Python program to test whether a number is within 100 of 1000 or 2000."

def within100(x):
    """Returns true if a number is within 100 of 1000 or 2000

    Args:
        x ([int]): [The number you want to check]
    """

    ans=False 

    if x>=900 and x<=1100:
        ans=True 

    if x>=1900 and x<=2100:
        ans=True 


    if ans==True:
        return True
    else:
        return False
x=float(input("Enter the number you want to check: "))
print(within100(x))