s2=input()
rs1=''
s3=sorted(s2)
for i in s3:
    if len(i)>len(rs1):
        rs1=i
print(rs1)
