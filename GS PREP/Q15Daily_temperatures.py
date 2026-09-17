# Daily Temperatures

# This is a very useful Goldman-style problem because it tests arrays + stack reasoning.

# Given daily temperatures, return how many days you have to wait until a warmer temperature.

# Example
# Input:
# [73, 74, 75, 71, 69, 72, 76, 73]

# Output:
# [1, 1, 4, 2, 1, 1, 0, 0]

# Explanation:

# 73 → warmer 74 after 1 day
# 74 → warmer 75 after 1 day
# 75 → warmer 76 after 4 days
# 71 → warmer 72 after 2 days
# 69 → warmer 72 after 1 day
# 72 → warmer 76 after 1 day
# 76 → no warmer day → 0
# 73 → no warmer day → 0
# Requirements

# Try for O(n) time.
def daily_temperatures(temperatures):
    stack = []  # stores indices
    result = [0] * len(temperatures)

    for i, temp in enumerate(temperatures):

        while stack and temperatures[stack[-1]] < temp:
            previous_index = stack.pop()
            result[previous_index] = i - previous_index

        stack.append(i)

    return result