def twoSum(arr, target):
    seen = {}
    for i in range(len(arr)):
        c = target - arr[i]
        if c in seen:
            return seen[c], i
        else:
            seen[arr[i]] = i
    return None