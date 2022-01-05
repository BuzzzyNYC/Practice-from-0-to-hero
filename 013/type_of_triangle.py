'''
Viết chương trình nhập vào ba số a, b, c. 
Nếu a, b, c là ba cạnh của một tam giác thì kiểm tra và hiển thị ra màn hình loại của tam giác.
Thuật toán:
Ba cạnh a, b, c của một tam giác phải thỏa mãn điều kiện là tổng hai cạnh bất kỳ luôn lớn hơn cạnh còn lại: a+b>c và a+c>b và b+c>a.
Tam giác vuông là tam giác có bình phương một cạnh bằng tổng bình phương hai cạnh còn lại: a*a==b*b+c*c hoặc b*b==a*a+c*c hoặc c*c== a*a+b*b
Tam giác đều là tam giác có ba cạnh bằng nhau: a==b và b==c
Tam giác cân là tam giác có hai cạnh bằng nhau: a==b hoặc a==c hoặc b==c
Tam giác tù là tam giác có một góc lớn hơn 90 độ. Từ điều kiện kiểm tra tam giác vuông, ta suy ra điều kiện để là tam giác tù là: a*a>b*b+c*c hoặc b*b>a*a+c*c hoặc c*c >a*a+b*b
Trường hợp còn lại sẽ là tam giác nhọn.
'''
try:
    a,b ,c = map(float, input("Nhap vao 3 canh cua mot tam giac cach nhau boi dau cach: ").split())

except:
    print("Invalid input")
    quit()
# Kiem tra dieu kien tien quyet a, b, c la 3 canh cua mot tam giac
if a + b > c and a + c > b and b + c > a:
    # Kiem tra 3 canh co phai tam giac vuong khong
    if a * a == b * b + c * c or b * b == a * a + c * c or c * c == a * a + b * b:
        loai_tam_giac = 'vuong'
    elif a == b and b == c and a == c:
        loai_tam_giac = 'deu'
    elif a == b or a == c or b == c:
        loai_tam_giac = "can"
    elif a*a>b*b+c*c or b*b>a*a+c*c or c*c >a*a+b*b:
        loai_tam_giac = 'tu'
    else:
        loai_tam_giac = "nhon"
    print("{}, {}, {} la ba canh cua mot tam giac {}".format(a, b, c, loai_tam_giac))
else:
    print("{}, {}, {} khong phai la 3 canh cua mot tam giac".format(a, b, c))

