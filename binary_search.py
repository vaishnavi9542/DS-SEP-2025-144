def binary_search(arr,val):
    low=0
    high=len(arr)
    while low<=high:
        mid=(low+high)//2
        if arr[mid]==val:
            return mid
        elif arr[mid]<=val:
            low=mid+1
        else:
            high=mid-1
    return -1
arr=list(map(int,input().split()))
val=int(input())
print(binary_search(arr,val))
