
while True:
    n = int(input("Nhap vao so nguyen n > 0: "))
    if n > 0: break

L = []

for i in range(n):
    x = float(input(f"Nhap phan tu thu {i + 1} : "))
    L.append(x)
    
print("danh sach so thuc : ",L)

# tim so lon nhat
print("So lon nhat trong danh sach : ", max(L))
#Tinh tong cac phan tu
print("Tong cac phan tu trong danh sach : ",sum(L))
#sap xep tang dan 
for i in range(0, n-1):
    for j in range(i+1, n):
        if L[i] > L[j]:
            temp = L[i]
            L[i] = L[j]
            L[j] = temp

print("danh sach sau khi sap xep la : ", L)
#diem so duong va am 
duong = 0
am = 0
for i in L:
    if i >= 0:
        duong+= 1
    else:
        am += 1

print("so phan tu duong trong danh sach la : ",duong)
print("so phan tu am trong danh sach la : ", am)
