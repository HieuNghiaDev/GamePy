def tong_chuoi_Sn(n):
    tong = 0
    for i in range(n+1):
        tong += 1 + 12*i + 1
    return tong

n = int(input("nhap vao n : "))
print("Tổng chuỗi S",n, "là: ",tong_chuoi_Sn(n))