# You are given API request logs sorted by timestamp:

# logs = [
#     (1, 200),
#     (2, 500),
#     (3, 200),
#     (4, 503),
#     (5, 200),
#     (10, 500),
#     (11, 200),
# ]

# Each entry is:

# (timestamp_in_seconds, status_code)

# You need to find the maximum number of 5xx errors that occurred within any 5-second window.

# For the above input:

# timestamp 1 → 5
# 500 errors:
# t=2
# t=4

# => 2 errors

# At timestamps 10–11:

# t=10 → 500
# => 1 error

# So the answer is:

# 2
# Important assumption

# The logs are sorted by timestamp.

# A window of 5 seconds means:

# current_timestamp - earliest_timestamp <= 5
# Example 2
# logs = [
#     (1, 500),
#     (2, 500),
#     (3, 200),
#     (6, 500),
#     (7, 500),
# ]

# Expected:

# 3

# Because the window [2, 7] contains:

# t=2 → 500
# t=6 → 500
# t=7 → 500

def max_5xx_in_window(logs):
    left = 0
    error_count = 0
    max_errors = 0

    for right in range(len(logs)):

        if logs[right][1] > 499 and logs[right][1]<600:
            error_count += 1
        # shrink window
        while logs[right][0] - logs[left][0] > 5:
            if logs[left][1] > 499 and logs[left][1]<600:
                error_count -= 1
            left += 1

        max_errors = max(max_errors, error_count)