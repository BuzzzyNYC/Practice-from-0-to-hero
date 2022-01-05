try:
    with open('007.txt', 'r', encoding='utf-8') as fileInp:
        name = fileInp.readline().rstrip('\n')
        current_age = int(fileInp.readline().rstrip('\n'))

    with open('007.txt', 'wb') as fileOut:
        stringTosave = "20 nam nua tuoi cua {} se la {}".format(name, current_age + 20)
        fileOut.write(stringTosave.encode('utf8'))

except:
    print("dinh dang file khong hop le!")