'''
Viết chương trình nhập vào từ bàn phím tên và chiều cao (cm) của hai bạn. 
Hiển thị ra màn hình thông báo bạn nào cao hơn.
'''
# Nhap ten va chieu cao cua nguoi thu nhat tren cung 1 dong

try:
    name1, height_student1 = input("Nhap ten, chieu cao cach nhau boi dau cach: ").split()
    #Ep kieu chieu cao sang so nguyen
    height_student1 = int(height_student1)
    # Nhap ten va chieu cao cua nguoi thu hai tren cung 1 dong
    name2, height_student2 = input("Nhap ten, chieu cao cach nhau boi dau cach: ").split()
    #Ep kieu chieu cao sang so nguyen
    height_student2 = int(height_student2)
except:
    print("Invalid input")
    quit()

# Thuc hien so sanh
if height_student1 > height_student2:
    print(name1, "cao hon", name2)
elif height_student1 == height_student2:
    print("Chieu cao cua", name1, "va", name2, "bang nhau")
else:
    print(name2, "cao hon", name1)
    