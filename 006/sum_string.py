'''
print("Nhap vao day cac so khac nhau cach nhau boi khoang trang: ")
day_so = input()
day_gia_tri = day_so.split()
isParseDone = False
try:
    danh_sach_so = map(int, day_gia_tri)
    tong_day_so = sum(danh_sach_so)
    isParseDone = True
except:
    print("Invalid input")

if isParseDone:
    print("Tong cua day so la:", tong_day_so)
'''



print("Nhap vao day cac so khac nhau cach nhau boi khoang trang: ")
day_so = input()
day_gia_tri = day_so.split()
print(day_gia_tri)
try: 
    danh_sach_so = map(int, day_gia_tri)
    tong_day_so = sum(danh_sach_so)
    print("Tong cua day so la:", tong_day_so)
except:
    print("Invalid input")

