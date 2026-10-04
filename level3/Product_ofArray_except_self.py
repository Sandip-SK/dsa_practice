# Given:

# nums = [1, 2, 3, 4]

# return:

# [24, 12, 8, 6]

# Because:

# 24 = 2 × 3 × 4
# 12 = 1 × 3 × 4
#  8 = 1 × 2 × 4
#  6 = 1 × 2 × 3
# Constraints
# O(n) time
# Do not use division
# Aim for O(1) extra space excluding the output array.
def product_except_self(nums):
    result = [1] * len(nums)

    # left → right
    for i in range(1, len(nums)):
        result[i] = result[i - 1] * nums[i - 1]
    # right → left
    right_product = 1
    for i in range(len(nums) - 1, -1, -1):
        result[i] *= right_product
        right_product *= nums[i]

    return result