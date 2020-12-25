"""10. Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn. 
    Sample value of n is 5
    Expected Result : 615"""

x=int(input('Enter the integer'))
a1=x
a2=int('{}{}'.format(x,x))
a3=int('{}{}{}'.format(x,x,x))

print(a1+a2+a3)


