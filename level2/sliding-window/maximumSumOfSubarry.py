# Given:

# nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]

# Find the maximum sum of a contiguous subarray.

# Expected answer:

# 6

# Because:

# [4, -1, 2, 1]

# has sum:

# 4 + (-1) + 2 + 1 = 6

# O(n3)
def brute_force_1(arr):
    max_sum = 0
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            max_sum = max(max_sum, sum(arr[i:j]))
    return max_sum

# O(n2)
def brute_force_2(arr):
    max_sum = arr[0]

    for i in range(len(arr)):
        curr_sum = arr[i]

        for j in range(i + 1, len(arr)):
            curr_sum += arr[j]
            max_sum = max(max_sum, curr_sum)

    return max_sum

#O(n)
def max_subarray(arr):
    curr_sum = 0
    max_sum = arr[0]
    for i in arr:
        curr_sum = max(i, curr_sum + i)
        max_sum = max(max_sum, curr_sum)
    return max_sum