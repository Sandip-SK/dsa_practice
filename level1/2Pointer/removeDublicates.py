# Given a sorted array:

# [1, 1, 2, 2, 3, 4, 4]

# Remove duplicates in-place and return the number of unique elements.

# Expected:

# 4

# Because the unique portion should become:

# [1, 2, 3, 4, ...]
# Requirements
# Don't create another array.
# Use O(1) extra space.
# The array is sorted.
def remove_duplicates(arr):
    if not arr:
        return 0
    pos = 1
    dub = arr[0]
    for i in range(1,len(arr)):
        if arr[i] != dub:
            dub = arr[i]
            arr[i],arr[pos] = arr[pos], arr[i]
            pos+=1
    return pos