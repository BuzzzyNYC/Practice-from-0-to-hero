'''
Write a program that display a triangle with size n from 1 - 9.
'''
try: 
    n = int(input())
except:
    print("Invalid input!")
    quit()
if n < 1 or n > 9:
    print("Please enter a number from 1 to 9!")
else:
    for row in range(1, n + 1):
        for col in range(1, row + 1):
            print(col, end=" ")
        print()