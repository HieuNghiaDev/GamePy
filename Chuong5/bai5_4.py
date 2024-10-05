thi_sinh = []
n = int(input("Nhap vao so thi sinh: "))

for i in range(n):
    while True:
        sbd = input("Nhap so bao danh: ")
        if len(sbd) != 5 or not sbd.isdigit():
            print("SBD phai bang 5 so va phai la so nguyen")
            continue
        hoten = input("Nhap ho ten thi sinh: ")
        if len(hoten) > 25:
            print("Ho ten khong duoc qua 25 ky tu")
            continue
        try:
            Dtoan = float(input("Nhap vao diem toan: "))
            if Dtoan < 0 or Dtoan > 10:
                print("Diem khong duoc nho hon 0 hoac lon hon 10")
                continue
        except ValueError:
            print("Diem phai la so thuc")
            continue
        try:
            DNvan = float(input("Nhap vao diem ngu van: "))
            if DNvan < 0 or DNvan > 10:
                print("Diem khong duoc nho hon 0 hoac lon hon 10")
                continue
        except ValueError:
            print("Diem phai la so thuc")
            continue

        thi_sinh.append({'SBD': sbd, 'hoten': hoten, 'DiemToan': Dtoan, 'DiemNguVan': DNvan})
        break

# Xuat danh sach thi sinh
print("Danh sach thi sinh")
for ts in thi_sinh:
    print(f"SBD: {ts['SBD']}\tTen: {ts['hoten']}\tDiem Toan: {ts['DiemToan']}\tDiem Ngu Van: {ts['DiemNguVan']}")

# Xuat danh sach thi sinh co tong diem > 10
print("Danh sach thi sinh co tong diem > 10:")
for ts in thi_sinh:
    tongd = ts['DiemToan'] + ts['DiemNguVan']
    if tongd > 10:
        print(f"SBD: {ts['SBD']}\tTen: {ts['hoten']}\tDiem Toan: {ts['DiemToan']}\tDiem Ngu Van: {ts['DiemNguVan']}")

# Danh sach thi sinh bi diem liet
print("Danh sach thi sinh bi diem liet:")
for ts in thi_sinh:
    if ts['DiemToan'] == 0 or ts['DiemNguVan'] == 0:
        print(f"SBD: {ts['SBD']}\tTen: {ts['hoten']}\tDiem Toan: {ts['DiemToan']}\tDiem Ngu Van: {ts['DiemNguVan']}")
