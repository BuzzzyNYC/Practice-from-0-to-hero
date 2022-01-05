'''
Viết chương trình nhập vào ba số a, b, c. Hiển thị ra màn hình cho biết a, b, c có là ba cạnh của một tam giác hay không.
Thuật toán: Ba cạnh a, b, c của một tam giác phải thỏa mãn điều kiện là tổng hai cạnh bất kỳ luôn lớn hơn cạnh còn lại. 
Tức là a+b>c và a+c>b và b+c>a.
input: 3 floats
output: " ... la ba canh cua mot tam giac"
'''
try:

    triangle_input = input("Nhap vao 3 so thuc canh cua mot tam giac: ").split()
    a, b, c = map(float, triangle_input)

# hoac: triangle_input = map(float, input("Nhap vao 3 canh: ").split())

except:
    print("invalid input")
    quit()

if a + b > c and a + c > b and b + c > a:
    print("{}, {}, {} la ba canh cua mot tam giac".format(a, b, c))
else:
    print("{}, {}, {} khong phai la ba canh cua mot tam giac".format(a, b, c))