# Problem: Minimum Size Subarray Sum

# Given an array of positive integers nums and a positive integer target, find the minimum length of a contiguous subarray whose sum is greater than or equal to target.

# If no such subarray exists, return 0.

# Examples:

# nums = [2,3,1,2,4,3], target = 7
# Output: 2

# Because:

# [4,3] → 7

# Another:

# nums = [1,4,4], target = 4
# Output: 1

# And:

# nums = [1,1,1,1], target = 10
# Output: 0
def brute_force(arr, target):
    min_length = len(arr) + 1

    for i in range(len(arr)):
        current_sum = 0

        for j in range(i, len(arr)):
            current_sum += arr[j]

            if current_sum >= target:
                min_length = min(min_length, j - i + 1)

    return min_length if min_length != len(arr) + 1 else 0

def min_subarray_len(nums, target):
    min_len = len(nums) + 1
    current_sum = 0
    left = 0

    for right in range(len(nums)):
        current_sum += nums[right]

        while current_sum >= target:
            min_len = min(min_len, right - left + 1)
            current_sum -= nums[left]
            left += 1

    if min_len > len(nums):
        return 0
    else:
        return min_len