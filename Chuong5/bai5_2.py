# msv = input("nhap vao ma sinh vien : ")
# tensv = input("Nhap vao ten sinh vien : ")
# lop = input("nhap lop : ")

# sinh_vien = {'Ma sinh vien' : msv, 'Hoten' : tensv,'lop': lop}

# print(sinh_vien)

# for i in sinh_vien:
#     print(i, ":", sinh_vien[i])

list_sv = []
n = int(input("nhap vao so luong sinh vien : "))

for i in range(n):
    msv = input("nhap vao ma sinh vien : ")
    tensv = input("Nhap vao ten sinh vien : ")
    lop = input("nhap lop : ")
    
    sinh_vien = {'Ma sinh vien' : msv, 'Hoten' : tensv,'lop': lop}
    list_sv.append(sinh_vien)

print(list_sv)

# for  in list_sv:
#     print(f"Ma SV : {i[msv]}, Ho ten : {i[tensv]}, lop : {i[lop]}")