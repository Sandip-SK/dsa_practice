# Problem 1: Two Sum (Warm-up, but judged strictly)
# 📌 Problem Statement

# You are given an array of integers nums and an integer target.

# Return indices of the two numbers such that they add up to target.

# Assumptions

# Exactly one valid solution exists

# You cannot use the same element twice

# 🔍 What I expect from you

# Reply with three sections (just like in a real interview):

# 1️⃣ Approach (plain English)
# Explain how you’ll solve it and why.

# 2️⃣ Complexity Analysis

# Time complexity

# Space complexity

# 3️⃣ Code (Python preferred)
# Clean, readable, production-style code.

def twoInteger(num, target):
    num_hash = {}
    for i, n in enumerate(num):
        complement = target - n
        if complement in num_hash:
            return [num_hash[complement], i]
        num_hash[n] = i
    return []

# Example usage:
nums = [2, 7, 11, 15]
target = 18
result = twoInteger(nums, target)
print(result)  # Output: [0, 1]