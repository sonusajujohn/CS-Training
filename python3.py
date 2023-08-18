n=int(input("Enter array size"))
a=[]
print("Enter array elements")

for i in range(n):
    a.append(int(input()))
m=[]
count=0
for i in range(n):
    if a[i]!=0:
        m.append(a[i])
    else:
        count=count+1
for i in range(count):
    m.append(0)
for i in range(n):
    print(m[i],end='')
