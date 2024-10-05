sokwh = int(input("nhap vao so kwh : "))

tien = 0

if sokwh <= 50:
    tien = sokwh * 2000
    print("so tien dien la : %d" %(tien))
elif sokwh <= 150:
    tien = 50 * 2000 + (sokwh - 50) * 2500
    print("so tien dien la : %d" %(tien))
elif sokwh <= 250:
    tien = tien = 50 * 2000 + (sokwh - 150) * 2500 + (sokwh - 250) * 3000
    print("so tien dien la : %d" %(tien))
elif sokwh <= 350:
    tien = tien = 50 * 2000 + (sokwh - 150) * 2500 + (sokwh - 250) * 3000 + (sokwh - 350) * 3500
    print("so tien dien la : %d" %(tien))
elif sokwh  > 350:
    tien = sokwh * 4000
    print("so tien dien la : %d" %(tien))