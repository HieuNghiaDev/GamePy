print("nhap vao scmt : ")
s = input()
count_s = len(s)

print(count_s)
if s.isnumeric() == True:
    if count_s >= 9 and count_s <= 11:
        print("la chuoi hop le")
else:
    print("la chuoi khong hop le")