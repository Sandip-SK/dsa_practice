# You are given a list of HTTP status codes:

# errors = [500, 404, 500, 503, 500, 404, 502, 503, 503, 503]

# Return the top 2 most frequent status codes.

# Expected output:

# [503, 500]
# Another example
# errors = [500, 500, 404, 404, 503]
# k = 2

# Possible output:

# [500, 404]

# If there is a tie, any order is acceptable.

# Constraints
# 1 <= len(errors) <= 10^5
# 1 <= k <= number of unique status codes

# Try to achieve better than O(n log n) if you can.
import heapq
errors = [500, 404, 500, 503, 500, 404, 502, 503, 503, 503]

def top_k_errors(errors, k):
    count = {}
    res = []
    for i in errors:
        if i not in count:
            count[i] = 1
        else:
            count[i] += 1
    # Min heap
    heap = []
    for status_code, frequency in count.items():
        heapq.heappush(heap, (frequency, status_code))
        if len(heap) > k:
            heapq.heappop(heap)

    return [status_code for frequency, status_code in heap]