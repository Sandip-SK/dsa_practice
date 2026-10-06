import heapq

def top_k_frequent(nums, k):
    count = {}
    min_heap = []
    for num in nums:
        count[num] = count.get(num, 0) + 1
    for num, count in count.items():
        heapq.heappush(min_heap, (count, num))
        if len(min_heap)>k:
            heapq.heappop(min_heap)
    return [num for count, num in min_heap]