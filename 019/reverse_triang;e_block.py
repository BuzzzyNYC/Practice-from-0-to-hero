'''
Write a program to display an up-side-down triangle with user's input n ranges from 1 - 9.
'''

try:
    n = int(input())
except:
    print("Invalid input")
    quit()
    
if n < 1 or n > 9:
    print("Please enter a number from 1 - 9!")
else:
    for row in range(n):
        for col in range(n - row, 0, -1):
            print(col, end=" ")
        print()