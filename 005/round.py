num_a = input()
num_b = input()
isParseDone = False
try:
    number_a = float(num_a)
    number_b = int(num_b)
    isParseDone = True
except:
    print("Invalid input")

if isParseDone:
    print('Dung format: {0:.{1}f}'.format(number_a, number_b))
    roundedNum = round(number_a, number_b)
    print('Dung round: ', roundedNum)