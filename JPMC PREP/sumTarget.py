# You are given a list of integers nums and an integer target.
# Return the indices of the two numbers whose sum equals target.
# You may assume:
# - There is exactly one solution.
# - You cannot use the same element twice.
# - Return the indices in any order.
# Example
# nums = [2, 7, 11, 15]
# target = 9

# Output:
# [0, 1]

# Because:
# nums[0] + nums[1]
# = 2 + 7
# = 9
def two_sum(nums, target):
    seen = {}

    for i, num in enumerate(nums):
        complement = target - num

        if complement in seen:
            return [seen[complement], i]

        seen[num] = i

    return None