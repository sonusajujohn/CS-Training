n = int(input("Enter the size of array"))
print("Enter the elements")
arr = []
for i in range(n):
    arr.append(int(input()))

for i in range(n):

    if ((i == 0 or arr[i - 1] < arr[i]) and (i == n - 1 or arr[i ] > arr[i+1])):
        print("The first +ve peak element")
        print(arr[i])
        
