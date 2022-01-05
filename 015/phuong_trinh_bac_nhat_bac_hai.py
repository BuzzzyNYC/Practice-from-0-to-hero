'''
Định dạng đầu vào
Gồm hai dòng:

Dòng đầu tiên chứa số 1 hoặc 2 tương ứng với:
Chức năng 1: giải phương trình bậc nhất
Chức năng 2: giải phương trình bậc hai
Dòng thứ hai chứa hệ số tùy thuộc vào chức năng được chọn ở dòng 1:
Chức năng 1: chứa hai số a, b lần lượt là hệ số của phương trình ax + b = 0, các hệ số cách nhau bởi khoảng trắng.
Chức năng 2: chứa ba số a, b, c lần lượt là hệ số của phương trình ax2 + bx + c = 0, các hệ số cách nhau bởi khoảng trắng.

Thuật toán:
Giải phương trình bậc nhất:
Phương trình vô số nghiệm khi: hệ số a, b đều bằng 0
Phương trình vô nghiệm khi: hệ số a bằng 0 và b khác 0
Các trường hợp còn lại phương trình có nghiệm duy nhất
Giải phương trình bậc hai:
Phương trình vô số nghiệm khi: hệ số a, b, c đều bằng 0
Phương trình vô nghiệm khi: hệ số a, b bằng 0, c khác 0 và trường hợp delta nhỏ hơn 0
Phương trình có nghiệm kép khi delta bằng 0
Phương trình có hai nghiệm phân biệt khi delta lớn hơn 0
'''

import math

#Khoi lenh co the phat sinh loi
try:   
   #Mo file voi mode='r' de doc file
   with open('file_to_read.txt', 'r') as fileInp:
       #Doc dong du lieu dau tien tu file
       #Su dung phuong thuc strip de loai bo ky tu xuong dong hay khoang trang
       dongDauTien = fileInp.readline().strip()
      
       #Truong hop 1: Giai phuong trinh bac nhat
       if dongDauTien == '1':
           #Doc dong du lieu thu hai tu file
           dongThuHai = fileInp.readline()
           a, b = map(float, dongThuHai.split())

           #Thuat toan giai phuong trinh bac nhat
           if a == 0:
               if b == 0:
                   thongBao = "Phuong trinh co vo so nghiem"
               else:
                   thongBao = "Phuong trinh vo nghiem"
           else:
               thongBao = "Phuong trinh co mot nghiem duy nhat: \nx = {}".format(-b / a)

       #Truong hop 2: Giai phuong trinh bac hai
       elif dongDauTien == '2':
           #Doc dong du lieu thu hai tu file
           dongThuHai = fileInp.readline()
           a, b, c = map(float, dongThuHai.split())
          
           #Thuat toan giai phuong trinh bac hai
           if a == 0:
               if b == 0:
                   if c == 0:
                       thongBao = "Phuong trinh co vo so nghiem"
                   else:
                       thongBao = "Phuong trinh vo nghiem"
               else:
                   thongBao = "Phuong trinh co mot nghiem duy nhat: \nx = {}".format(-c / b)
           else:
               #Tinh delta
               delta = b * b - 4 * a * c
               #Kiem tra cac truong hop cua delta
               if delta > 0:
                   x1 = float((-b + math.sqrt(delta)) / (2 * a))
                   x2 = float((-b - math.sqrt(delta)) / (2 * a))
                   thongBao = "Phuong trinh co hai nghiem phan biet la: \nx1 = {} \nx2 = {}".format(x1, x2)
               elif delta == 0:
                   x = -b / (2 * a)
                   thongBao = "Phuong trinh co nghiem kep: \nx1 = x2 = {}".format(x)
               else:
                   thongBao = "Phuong trinh vo nghiem"

       #Truong hop khong chon dung chuc nang
       else:
           thongBao = "Vui long chon mot trong hai chuc nang:\n1. Giai phuong trinh bac nhat\n2.Giai phuong trinh bac hai"

#Khoi lenh duoc thuc thi khi xay ra loi "Khong tim thay file input"
except FileNotFoundError:
   thongBao = "Khong tim thay file input!"

#Khoi lenh duoc thuc thi khi xay ra loi "Sai dinh dang dau vao"
except:
   thongBao = "Dinh dang dau vao khong hop le!"

#Mo file voi mode='w' de ghi file
with open('file_out.txt', 'wb') as fileOut:
   #Xuat thong bao ra file out
   fileOut.write(thongBao.encode('utf8'))