def nhap():
    so_bao_danh = input("Nhập số báo danh (5 chữ số): ")
    while not (so_bao_danh.isdigit() and len(so_bao_danh) == 5):
        so_bao_danh = input("Số báo danh không hợp lệ. Nhập lại (5 chữ số): ")

    ho_ten = input("Nhập họ và tên thí sinh (không quá 25 ký tự): ")
    while len(ho_ten) > 25:
        ho_ten = input("Họ và tên không hợp lệ. Nhập lại (không quá 25 ký tự): ")

    diem_toan = float(input("Nhập điểm Toán (0 - 10): "))
    while diem_toan < 0 or diem_toan > 10:
        diem_toan = float(input("Điểm Toán không hợp lệ. Nhập lại (0 - 10): "))

    diem_tieng_viet = float(input("Nhập điểm Tiếng Việt (0 - 10): "))
    while diem_tieng_viet < 0 or diem_tieng_viet > 10:
        diem_tieng_viet = float(input("Điểm Tiếng Việt không hợp lệ. Nhập lại (0 - 10): "))

    return {
        "so_bao_danh": so_bao_danh,
        "ho_ten": ho_ten,
        "diem_toan": diem_toan,
        "diem_tieng_viet": diem_tieng_viet
    }

def nhapslsv():
    danh_sach = []
    so_luong = int(input("Nhập số lượng thí sinh: "))
    for i in range(so_luong):
        thi_sinh = nhap()
        danh_sach.append(thi_sinh)
    return danh_sach

def hienthisv(danh_sach):
    print("\nDanh sách thí sinh:")
    for ts in danh_sach:
        print(f"SBD: {ts['so_bao_danh']}, Họ tên: {ts['ho_ten']}, Điểm Toán: {ts['diem_toan']}, Điểm Tiếng Việt: {ts['diem_tieng_viet']}")

def tongdiem(danh_sach):
    print("\nDanh sách thí sinh có tổng điểm lớn hơn 10:")
    for ts in danh_sach:
        if ts['diem_toan'] + ts['diem_tieng_viet'] > 10:
            print(f"SBD: {ts['so_bao_danh']}, Họ tên: {ts['ho_ten']}, Tổng điểm: {ts['diem_toan'] + ts['diem_tieng_viet']}")

def liet(danh_sach):
    print("\nDanh sách thí sinh có điểm liệt (ít nhất một điểm 0):")
    for ts in danh_sach:
        if ts['diem_toan'] == 0 or ts['diem_tieng_viet'] == 0:
            print(f"SBD: {ts['so_bao_danh']}, Họ tên: {ts['ho_ten']}, Điểm Toán: {ts['diem_toan']}, Điểm Tiếng Việt: {ts['diem_tieng_viet']}")

def main():
    danh_sach = nhap()
    hienthisv(danh_sach)
    tongdiem(danh_sach)
    liet(danh_sach)

main()
