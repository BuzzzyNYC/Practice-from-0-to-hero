'''
Viết chương trình nhập vào từ bàn phím một dãy số nguyên với độ dài bất kỳ, dãy số nằm trên 1 dòng, 
các số cách nhau bởi khoảng trắng. Tính tổng của dãy số và hiển thị ra màn hình (Có xử lý ngoại lệ đầu vào).
'''
try: 
    num1, phep_tinh, num2 = input("Nhap vao phep tinh: ").split()
    num1 = float(num1)
    num2 = float(num2)
except:
    print("Vui long nhap lai!")
    quit()

ket_qua = 0

if phep_tinh == "+":
    ket_qua = num1 + num2
elif phep_tinh == "-":
    ket_qua = num1 - num2
elif phep_tinh == "*":
    ket_qua = num1 * num2
elif phep_tinh == ":" or phep_tinh == "/":
    if num2 == 0:
        print("So bi chia phai khac 0")
    else:
        ket_qua = round(num1 / num2, 3)

if ket_qua != None:
    print("{} {} {} = {}".format(num1, phep_tinh, num2, ket_qua))
