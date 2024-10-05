from datetime import datetime
import math

def bai4_1():
    for i in range(0,100,1):
        print("hello", i)

# bai4_1()

def bai4_2():
    year = datetime.now().year
    while True:
        namsinh = int(input("Nhap vao nam sinh : "))
        if namsinh > 1900 and namsinh <= year:
            tuoi = year - namsinh
            break
        print("Nam sinh khong hop le ")
    print("tuoi cua ban la ", tuoi)

# bai4_2()

def bai4_3():
    h = int(input("Nhap vao gio hien tai : "))
    m = int(input("Nhap vao phut hien tai : "))
    s = int(input("Nhap vao giay : "))
    k = int(input("Nhap vao so k : "))
    
    sum_s = (h * 3600) + (m * 60) + (s + k)
    
    new_h = (sum_s // 3600)
    new_m = (sum_s % 3600) // 60
    new_s = sum_s % 60
    
    print(new_h, " gio " ,new_m, " phut" ,new_s, " giay ")

# bai4_3()

def ucln(a, b):
    while b != 0:
        a, b = b, a%b
    return a

def bai4_4():
    integer1 = int(input("Nhap vao so nguyen thu nhat : "))
    integer2 = int(input("Nhap vao so nguyen thu hai : "))
        
    if integer1 != 0 and integer2 != 0:
        a = ucln(a = integer1, b = integer2)
    print(a)
    
# def bai4_4():
    
#     while True:
#         a = int(input("nhap vao so a : "))
#         if a != 0: break
#     while True:
#         b = int(input("nhap vao so b : "))
#         if b != 0: break
        
#     ucln = 0
#     i = 0
#     if a > b:
#         c = b
#     else:
#         c= a

#     for i in range(1, c+1,1):
#         if a % i == 0 and b % i == 0:
#             ucln = i
    
#     print("Uoc chung lon nhat : ", ucln)
    
# bai4_4()

def bai4_5():
    for i in range(1,21):
        for j in range(1,34):
            k = 100 - i - j
            if (5*i) +(3*j) + (k/3) == 100:
                print("Trau dung : ", i, "trau nam ",j, "trau gia : ", k)

# # bai4_5()

# def bai4_6(n):
#     k = 0
#     count = 0
#     while n != 0:
#        count += 1
#        k += n%10
#        n = int(n/10)
    
#     return k,count

# n = int(input("nhap vao so n "))
# k,count = bai4_6(n)
# print("so",n," co",count," chu so va tong la :",k)

def bai4_7():
    # i = 1
    s = 0
    for i in range(1,2004):
        s += i*(i+1)
    print(s)

bai4_7()

def bai4_8():
    x = int(input("nhap vao x : "))
    n = int(input("nhap va0 n : "))
    
    s = 0
    for i in range(0,n):
        s += x**(2*i + 1)
    
    print(s)

# bai4_8()

        
            
            

    