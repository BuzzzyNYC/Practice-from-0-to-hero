'''
Viết chương trình giải phương trình bậc hai với các hệ số được nhập từ bàn phím và hiển thị kết quả ra màn hình.
'''
'''
input: Gồm một dòng duy nhất chứa ba số a, b, c lần lượt là hệ số của phương trình ax2 + bx + c = 0, 
các hệ số cách nhau bởi khoảng trắng.
output: Gồm nhiều dòng hiển thị tùy theo các trường hợp như sau:

Nếu phương trình vô nghiệm: Phuong trinh vo nghiem

Nếu phương trình có vô số nghiệm: Phuong trinh co vo so nghiem

Nếu phương trình có một nghiệm duy nhất: Phuong trinh co mot nghiem duy nhat: x = {x1}

Nếu phương trình có nghiệm kép: Phuong trinh co nghiem kep: x1 = x2 = {x1}

Nếu phương trình có hai nghiem phan biet: Phuong trinh co hai nghiem phan biet: x1 = {x1}, x2 = {x2}

Thuật toán:
Phương trình vô số nghiệm khi: hệ số a, b, c đều bằng 0
Phương trình vô nghiệm khi: hệ số a, b bằng 0, c khác 0 và trường hợp delta nhỏ hơn 0
Phương trình có nghiệm kép khi delta bằng 0
Phương trình có hai nghiệm phân biệt khi delta lớn hơn 0
'''
#Import thu vien math de su dung ham sqrt tinh can bac 2
import math

try: 
    #Su dung ham map() va float de ep kieu du lieu sang so thuc
    a, b, c = map(float, input("Nhap vao 3 so: ").split())
except:
    print("Invalid input")
    quit()

if a == 0:
    if b == 0:
        if c == 0:
            print("Phuong trinh co vo so nghiem")
        else:
            print("Phuong trinh vo nghiem")
    else:
        print("Phuong trinh co mot nghiem duy nhat: \nx = {}".format(-c / b))

else:
    # Tinh delta
    delta = b * b - 4 * a * c
    # Kiem tra cac truong hop cua delta
    if delta > 0:
        x1 = round(float((-b + math.sqrt(delta)) / (2 * a)), 3)
        x2 = round(float((-b - math.sqrt(delta)) / (2 * a)), 3)
        print("Phuong trinh co hai nghiem phan biet la: \nx1 = {} \nx2 = {}".format(x1, x2))
    elif delta == 0:
        x = -b / (2 * a)
        print("Phuong trinh co nghiem kep: \nx1 = x2 = {}".format(x))
    else:
        print("Phuong trinh vo nghiem")
    
    
        