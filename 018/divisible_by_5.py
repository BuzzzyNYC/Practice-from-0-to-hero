'''
Write a program that prints all the number divisible by 5 (not more than 10 numbers) within the range of num1, num2
:type: int num1, num2 (num1 <= num2)
:rtype: int seperated by a space
'''
try:
    num1 = int(input())
    num2 = int(input())
except:
    print("Invalid input!")
    quit()
if num1 > num2:
    print("num1 has to be less than or equal to num2")
else:
    res = 0
    for i in range(num1, num2 + 1):
        if i % 5 == 0:
            res += 1
            if res > 10:
                print("\nThe result has reached 10 numbers divisible by 5")
                # break out of loop
                break
            print(i, end=" ")
if res == 0:
    print("There's no number divisible by 5")
