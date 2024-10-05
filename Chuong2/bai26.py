print("nhap chuoi thu 1 : ")
s1 = input()
print("Nhap chuoi thu 2 : ")
s2 = input()

if s2 in s1:
    x = s1.find(s2)
    print(x)
else:
    print("Khong tim thay")