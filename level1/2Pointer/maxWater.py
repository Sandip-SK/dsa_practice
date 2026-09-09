# Given an array height, where each element represents a vertical line, find two lines that together with the x-axis form a container that holds the maximum amount of water.

# Example:

# height = [1,8,6,2,5,4,8,3,7]

# Output = 49

# The two lines are:

# 8 and 7

# with width:

# 8 - 1 = 7

# So:

# area = min(8, 7) × 7
#      = 49
def max_area(height):
    left = 0
    right = len(height) - 1
    max_area = 0
    current_area = 0
    while left < right:
        current_area = min(height[left], height[right]) * (right-left)
        max_area = max(max_area, current_area)
        if height[left] > height[right]:
            right -= 1
        else:
            left += 1
    return max_area