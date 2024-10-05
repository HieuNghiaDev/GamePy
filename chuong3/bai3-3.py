import math

a = float(input("nhap a = "))
b = float(input("nhap b = "))
c = float(input("nhap c = "))

delta = b**2 -(4*a*c)

if delta > 0:
    x1 = (-b + math.sqrt(delta))/2*a
    x2 = (-b - math.sqrt(delta))/2*a
    print("PT co 2 nghiem x1 = %f" %(x1) + " x2 = %f"%(x2))
elif delta == 0:
    x = (-b)/2*a
    print("PT co 2 ngiem kep x1 = x2 = ",x)
else:
    print("PT vo nghiem")
