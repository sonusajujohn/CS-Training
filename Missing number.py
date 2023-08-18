numbers = []
n=int(input("Enter the number of elements\n"))
print("Enter the elements in the array:")
for i in range(n):
    numbers.append(int(input()))

# Find the smallest missing positive integer
missnum = 1
for num in numbers:
    if num == missnum:
        missnum += 1
    else:
        break

print("The smallest missing positive integer is:", missnum)
