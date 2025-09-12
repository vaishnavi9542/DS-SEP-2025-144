def binary_search(arr, val):
    low = 0
    high = len(arr) - 1 
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == val:
            return mid
        elif arr[mid] < val:
            low = mid + 1
        else:
            high = mid - 1
    return -1
arr = list(map(int, input("Enter sorted array: ").split()))
val = int(input("Enter value to search: "))
result = binary_search(arr, val)
if result != -1:
    print(f"Element found at index {result}")
else:
    print(f"Element not found")
