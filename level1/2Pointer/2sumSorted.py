# Given a sorted array, return the indices of two numbers whose sum equals the target. Assume exactly one solution exists.

# Example:

# nums = [2, 7, 11, 15]
# target = 9

# Output: [0, 1]

# Now consider:

# nums = [1, 1, 2, 3, 4]
# target = 5

def two_sum_sorted(nums, target):
    left = 0
    right = len(nums)-1

    while left < right:
        if nums[left] + nums[right] == target:
            return left, right
        elif nums[left]+nums[right] > target:
            right -= 1
        else:
            left += 1
    return None
