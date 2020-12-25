"""7. Write a Python program to accept a filename from the user and print the extension of that"""
x=list(map(str,input("Enter the file name: ").split('.'))
        )

print('The file format is {}'.format(x[1]))



