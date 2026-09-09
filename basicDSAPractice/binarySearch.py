def binarySearch(arr, target):
    low = 0
    high = len(arr) - 1

    while high>=low:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif target > arr[mid]:
            low = mid+1
        elif target<arr[mid]:
            high = mid-1
        
    return -1

def binarySearchReccursive(arr, low, high, target):
    if low > high:
        return -1
    if low == high:
        if arr[low] == target:
            return low
        else:
            return -1
    else:
        mid = (low+high)//2
        if target == arr[mid]:
            return mid
        elif target<arr[mid]:
            binarySearchReccursive(arr, low, mid-1, target)
        elif target>arr[mid]:
            binarySearchReccursive(arr, mid+1, high, target)