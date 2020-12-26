"""19. Write a Python program to get a new string from a given string where "Is" has been added to the front. If the given string already begins with "Is" then return the string unchanged."""

def stringCheck(x):
    """Return a new string by adding "Is" in front of it,
    If the string already begins with "Is" then it returns 
    the string as it is.
    Input: string[str]:[Old String]"""

    y=list(map(str,x.split(" ")))
    print(y)

    if y[0]=="Is":
        return x
    else:
        return "Is " + x
    

x=input("Enter the old string: ")

print(stringCheck(x))


