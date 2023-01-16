n=int(input())
s=input().split()
rs=''
if n<2:
    print(s[0])
s.sort()
chk=s[0]
print(chk)
s.remove(s[0])
print(s)
for i in range(len(chk)):
    flag=0
    for j in s:
        if chk[i]==j[i]:

            flag+=1
        else:
            break
    if flag==len(s):
            rs+=chk[i]
    else:
            break
if len(rs)==0:
        print(-1)
else:
        print(rs)











