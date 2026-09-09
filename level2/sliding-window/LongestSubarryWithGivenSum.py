# Given an array of positive integers and a target k, find the length of the longest contiguous subarray whose sum equals k.

# Example:

# nums = [1, 2, 1, 1, 1, 3]
# k = 3

# Answer:

# 3

# Because:

# [1, 1, 1]

# has length 3 and sum 3.

# But there is another:

# [1, 2]

# with length 2.

# So we want the longest.
def brute_force(arr, k):
    max_length = 0
    for i in range(len(arr)):
        for j in range(i + 1, len(arr) + 1):
            if sum(arr[i:j]) == k:
                max_length = max(max_length, j - i)
    return max_length

def longest_subarray_with_given_sum(arr, k):
    left = 0
    current_sum = 0
    max_length = 0

    for right in range(len(arr)):
        # sum<k
        current_sum += arr[right]

        while current_sum > k:
            current_sum -= arr[left]
            left += 1

        if current_sum == k:
            max_length = max(max_length, right - left + 1)
    return max_length