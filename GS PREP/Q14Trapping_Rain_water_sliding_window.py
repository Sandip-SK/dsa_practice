# Trapping Rain Water

# This is a high-priority medium-level problem because it tests two-pointer reasoning.

# Given an array representing heights of bars:

# Input:
# [0,1,0,2,1,0,1,3,2,1,2,1]

# Output:
# 6

# The bars trap water between them.

# Question: Return the total amount of trapped water.

# Try to solve it in O(n) time and O(1) extra space.
input = [0,1,0,2,1,0,1,3,2,1,2,1]
def trapped_rainwater(arr):
    left = 0
    right = len(arr) - 1

    left_max = 0
    right_max = 0
    total_water = 0

    while left < right:

        if arr[left] <= arr[right]:

            if arr[left] >= left_max:
                left_max = arr[left]
            else:
                total_water += left_max - arr[left]

            left += 1

        else:

            if arr[right] >= right_max:
                right_max = arr[right]
            else:
                total_water += right_max - arr[right]

            right -= 1

    return total_water

print(trapped_rainwater(input))