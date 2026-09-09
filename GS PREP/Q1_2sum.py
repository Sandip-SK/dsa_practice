# Problem 1 — HashMap / Arrays

# Two Sum

# Given an integer array nums and an integer target, return the indices of the two numbers such that they add up to target.

# You may assume that:

# Each input has exactly one solution.
# You cannot use the same element twice.
# The answer can be returned in any order.

# Example 1:

# Input:  nums = [2, 7, 11, 15], target = 9
# Output: [0, 1]

# Example 2:

# Input:  nums = [3, 2, 4], target = 6
# Output: [1, 2]

# Constraints:

# 2 <= len(nums) <= 10^5
# -10^9 <= nums[i] <= 10^9
# -10^9 <= target <= 10^9

def two_sum(arr, target):
    seen = {}
    complement = 0
    for i in range(len(arr)):
        complement = target - arr[i]
        if complement in seen:
            return [seen[complement], i]
        else:
            seen[arr[i]] = i
    return None