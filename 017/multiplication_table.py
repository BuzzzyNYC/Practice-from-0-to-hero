'''
Write a multiplication table with exceptional handling
:type: int from 1 to 9
if input is out of this range --> print("This is a multiplication table from 1 to 9")
Other cases not complying input requirement --> print("Invalid input!")
:rtype: 9 rows showing the multiplication operation.
'''
try:
# Prompt user's input
    n = int(input("Enter a number: "))
except:
    print("Invalid input! Please enter number from 1 - 9")
    quit()
# Using if-condition to identify cases range outside of 1-9
if n < 1 and n > 9:
    print("This is a multiplication from 1 to 9!")
else:
    for i in range(1, 10):
        print("{} x {} = {}".format(n, i, n * i))
