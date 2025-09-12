def linear_search(arr,val):
    for i in arr:
        if i==val:
            return True
    return False
arr=list(map(int,input().split()))
val=int(input())
print(linear_search(arr,val))
