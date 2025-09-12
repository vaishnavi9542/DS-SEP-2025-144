def partition(arr,low,high):
    pivot=arr[high]
    i=low-1
    for j in range(low,high):
        if arr[j]<pivot:
            i+=1
            arr[i],arr[j]==arr[j],arr[i]
    arr[i+1],arr[high]=arr[high],arr[i+1]
    return i+1  
def quicksort(arr,low,high):
    if low<high:
        k=partition(arr,low,high)
        quicksort(arr,low,k-1)
        quicksort(arr,k+1,high)
arr=list(map(int,input().split()))
n=len(arr)
print("original array:",arr)
quicksort(arr,0,n-1)
print("sorted array:",arr)
