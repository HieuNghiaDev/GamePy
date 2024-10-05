list_HH = []
n = int(input("Nhap so luong hang hoa : "))

for i in range(n):
    tenhang = input("nhap vao ten hang hoa : ")
    soluong = int(input("Nhap vao so luong : "))
    giaban = input("Nhap vao gia ban : ")
    
    hangHoa = {'tenhanghoa':tenhang, 'soluong':soluong, 'giaban':giaban}
    list_HH.append(hangHoa)

#tinh tong so luong hang hoa 
sl = 0
for hh in list_HH:
    sl = sl + hh['soluong']

print(list_HH)
print("Tong so luong hang hoa da nhap la : ",sl)
#hien thi thong tin cac mat hang co sl < 10
for hh in list_HH:
    if hh['soluong'] < 10:
        print("ten hang hoa : ",hh['tenhanghoa'],'\t',"so luong : ",hh['soluong'],'\t',"Gia ban",hh['giaban'])

#hien thi thong tin cac mat hang co so luong lon hon > 50
for hh in list_HH:
    if hh['soluong'] > 50:
        print("ten hang hoa : ",hh['tenhanghoa'],'\t',"so luong : ",hh['soluong'],'\t',"Gia ban",hh['giaban'])

