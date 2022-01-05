'''
su dung read(): lenh doc toan bo file
'''

# Mo file voi mode='r' (read) to read file
with open('file_to_read.txt', 'r') as read_file:
    #Dung ham read() doc toan bo du lieu tu file
    toanBoFile = read_file.read()

#Dung ham splitlines() cat du lieu theo tung dong va luu thanh danh sach
danhSachCacDong = toanBoFile.splitlines()

#Dung ham join() noi cac dong du lieu lai cach nhau 1 khoang trang
noiDungHoanChinh = ' '.join(danhSachCacDong)

#Mo file voi mode='w' de ghi file
with open('file_out.txt', 'w') as file_Out:

   #Ghi noi dung vao file
   file_Out.write(noiDungHoanChinh)

'''
su dung readlines(): lenh doc tung dong
'''
try:

    with open('file_to_read.txt', 'r', encoding='utf-8') as read_file:
        noi_dung = read_file.readlines()
        noi_dung_tren_mot_dong = ' '.join(noi_dung).replace('\n', '')

    file_out = open('file_output.txt', 'wb')
    file_Out.write(noi_dung_tren_mot_dong.encode('utf8'))
except:
    print("Loi doc/ghi file")
    