# Array and Hashing
# Brute Force
def contains_duplicate(nums):
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] == nums[j]:
                return True
    return False

# optizied
def contains_dublicates_op(nums):
    h = dict()
    for i in nums:
        if i in h:
            return True
        else:
            h[i] = 1
    return False

def contains_duplicates_op_2(nums):
    seen = set()
    for num in nums:
        if num in seen:
            return True
        seen.add(num)
    return False

def contains_duplicates_op_3(nums):
    return len(nums) != len(set(nums))