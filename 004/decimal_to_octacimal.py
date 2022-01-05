# print("Enter a number in decimal:")
# number_in_decimal = int(input())

# print("So thap phan %d trong he bat phan la %o" % (number_in_decimal, number_in_decimal))

# try:
#     a_decimal = int(input("Enter a decimal: "))
#     num = a_decimal
#     res = 0
#     while num > 0:
#         res = res*10 + num % 8
#         num //= 8

#     print("He bat phan cua", a_decimal, "la", res)
# except:
#     print("Invalid input")

number = input("Enter a number ")
isParseDone = False
try:
    decimal_num = int(number)
    isParseDone = True
except:
    print("Invalid input")

if isParseDone:
    print("So thap phan %d trong he bat phan la %o" % (decimal_num, decimal_num))


