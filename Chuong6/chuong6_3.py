def chuanHoa(s):
    list_s = s.split()
    s2 = ''
    for i in list_s:
        if i != '':
            s2 += i + ' '
    return s2.title()

s = 'le    hieu nghiA'
print(chuanHoa(s))