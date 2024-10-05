import math

def soNguyenTo(snt):
    if snt < 2:
        return False
    for i in range(2, int(math.sqrt(snt)) + 1):
        if snt % i == 0:
            return False
    return True

n = int(input("Nhap vao n : "))
if soNguyenTo(n):
    print(f"{n} la so nguyen to.")
else:
    print(f"{n} khong phai la so nguyen to.")
