from collections import Counter

print("nhap vao chuoi s ")
s = input()
print("nhap vao chuoi e : ")
e = input()

count = Counter(s)[e]

print(f"so lan ly tu '{e}' xuat hien trong chuoi la : {count}")