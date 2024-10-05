import math

def soNguyenTo(snt):
    if snt < 2:
        return False
    for i in range(2, int(math.sqrt(snt)) + 1):
        if snt % i == 0:
            return False
    return True

def xuly(n):
    for i in range(1, n + 1):
        if soNguyenTo(i) == True and soNguyenTo(i) < 100:
            print(i)
    
    
n = int(input("Nhap vao n : "))
xuly(n)