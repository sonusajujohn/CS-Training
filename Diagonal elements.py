r=int(input("Enter rows"))
c=int(input("Enter columns"))

m=[] 
print("Enter elements")
for i in range(r):
 a =[]
 for j in range (r):
   a.append(int(input()))
 m.append(a)  
        
for i in range(r):
 for j in range(c):
    print(m[i][j],end=" ")
 print()

 print("Diagonal elements")
 for i in range(r):
    for j in range(c):
        if (i==j):
         { 
        print(m[i][j],end=" ")
         }
        else:
         print(end=" ")
    print()