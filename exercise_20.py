"20. Write a Python program to get a string which is n (non-negative integer) copies of a given string."

def multipleString(sentence,n):
    """Assumes n is (non-negative integer) 
    Returns multiple copies of sentence

    sentence[str]:[The sentence you input]
    n [int]:[Non-negative number]
    """

    return sentence*n
        


sentence=input("Enter the string you want to copy: ")

n=int(input("Enter the number of the copies: "))

print(multipleString(sentence,n))




