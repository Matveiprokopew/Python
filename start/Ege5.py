spisok=[]
a=input('Введите число= ') 
for i in range(len(a)):
    spisok.append(a[i])
    print(spisok)
s1=int(spisok[0])+int(spisok[1])
s2=int(spisok[1])+int(spisok[2])
if s1>s2:
    v=str(s1)+str(s2)
else:
    v=str(s2)+str(s1)
print(v)
#14 12
