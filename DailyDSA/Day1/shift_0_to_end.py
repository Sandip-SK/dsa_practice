# The Two-Pointer Technique
# Prompt: Given an integer array nums, move all 0s to the end of it while maintaining the relative order of the non-zero elements.
# Constraint: You must do this in-place without making a copy of the array (Space Complexity must be $O(1)$).

def move_0(nums):
    slow = 0
    for fast in range(len(nums)):
        if nums[fast] != 0:
            #swap
            nums[fast], nums[slow] = nums[slow], nums[fast]
            slow = slow + 1
    return nums