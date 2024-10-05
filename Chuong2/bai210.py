x = input("nhap mail : ")
x = x.strip()
if( x.count("@",0,len(x)) != 1):
    print("mail khong hop le ")
else:
    a = x.find("@",0,len(x))
    b = x.find(".",0,len(x))
    if(a == 0):
        print("phia truoc @ khong co gia tri")
    else:
        if (a == b+1):
            print("phia sau @ khong co gi den . ")
        else:
            if(b == len(x)):
                print("phia sau . khong co gi")
            else:
                print("mail hop le")
