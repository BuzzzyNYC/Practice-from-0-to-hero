n = int(input())
if n < 0:
    print("Try again with an integer")
else:
    res = 1
    for i in range(1, n + 1):
        res *= i
    print(res)