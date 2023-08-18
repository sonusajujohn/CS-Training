a=[0,1,2,0,8,5]
s=6
pos=0
for i in range(s):
    if(a[i]!=0):
         a[pos]=a[i]
     
  pos=pos+1

while(pos<s):
    a[pos=pos+1]=0       