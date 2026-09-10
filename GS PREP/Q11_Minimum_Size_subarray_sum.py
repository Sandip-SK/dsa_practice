# Given an array of positive integers nums and a positive integer target, return the minimum length of a contiguous subarray whose sum is greater than or equal to target.

# If no such subarray exists, return 0.

# Example 1
# nums = [2, 3, 1, 2, 4, 3]
# target = 7

# Output:

# 2

# Because:

# [4, 3] → 7
# Example 2
# nums = [1, 4, 4]
# target = 4

# Output:

# 1
# Example 3
# nums = [1, 1, 1, 1]
# target = 10

# Output:

# 0
# Constraints
# 1 <= target <= 10^9
# 1 <= len(nums) <= 10^5
# 1 <= nums[i] <= 10^5

# Target: O(n) time.
def min_size_subarray_sum(arr, target):
    left = 0
    curr_sum = 0
    min_len = len(arr)
    for right in range(len(arr)):
        curr_sum = curr_sum + arr[right]
        while curr_sum >= target and left<=right:
            min_len = min(min_len, right-left+1)
            curr_sum = curr_sum - arr[left]
            left += 1
    if min_len == len(arr):
        return 0
    return min_len