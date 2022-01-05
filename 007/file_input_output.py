'''
Nhập từ file input {tên}, {tuổi hiện tại} và xuất ra file output

Note: readline(): read the text file line by line and return all the lines as strings.
readlines(): read all the lines of the text file and return them as a list of strings.
'''
try:
    with open('input.txt', 'r') as fileInp:
        name = fileInp.readline().rstrip('\n')
        current_age = int(fileInp.readline().rstrip('\n'))

    with open('input.txt', 'w') as fileOut:
        fileOut.write("20 nam nua tuoi cua {} se la {}".format(name, current_age + 20))
except:
    print("File not found!")