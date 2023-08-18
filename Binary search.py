def findpeak(arr,n):
    f=0
    r=n-1
    while f<=r:
        mid = (f + r) // 2
        if(mid == 0 or arr[mid - 1] <= arr[mid]) and (mid == n-1 or arr[mid + 1] <= arr[mid]):
            break
        if mid>0 and arr[mid - 1]>arr[mid]:
            r=mid-1
        else:
            f=mid+1
    return mid
arr = [100,-3,2,4,250,0]
n=len(arr)
print("Index of peak point is",findpeak(arr,n))



