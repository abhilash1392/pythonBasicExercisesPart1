"22. Write a Python program to count the number 4 in a given list."

def listCountFour(x):
    """The following program counts the number of 4 in the list"""
    count=0
    for i in x:
        if i==4:
            count+=1

    return count


print(listCountFour([1,2,3,4,3,4,5,4,5]))




