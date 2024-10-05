print("nhap ma sinh vien : ")
msv = input()
print("nhap ho ten sinh vien : ")
htsv = input()
drl = int(input("nhap diem ren luyen : "))

if drl >= 90:
    print("--------------------------")
    print("ma sinh vien : ",msv)
    print("ho ten sinh vien : ",htsv)
    print("hanh kiem xuat sac")
elif drl >= 80 and drl < 90:
    print("--------------------------")
    print("ma sinh vien : ",msv)
    print("ho ten sinh vien : ",htsv)
    print("hanh kiem Tot")
elif drl >= 65 and drl < 80:
    print("--------------------------")
    print("ma sinh vien : ",msv)
    print("ho ten sinh vien : ",htsv)
    print("hanh kiem kha")
elif drl >= 50 and drl < 65:
    print("--------------------------")
    print("ma sinh vien : ",msv)
    print("ho ten sinh vien : ",htsv)
    print("hanh kiem trung binh")
else:
    print("--------------------------")
    print("ma sinh vien : ",msv)
    print("ho ten sinh vien : ",htsv)
    print("hanh kiem yeu")