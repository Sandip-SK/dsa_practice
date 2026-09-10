# You are given student scores:

# scores = [
#     ("Alice", 90),
#     ("Bob", 80),
#     ("Alice", 70),
#     ("Bob", 100),
#     ("Alice", 95),
#     ("Bob", 90),
#     ("Alice", 85),
#     ("Bob", 75),
#     ("Alice", 100),
#     ("Bob", 95),
# ]

# Each student has at least 5 scores.

# Return the student with the highest average of their top 5 scores.

# For example:

# Alice → top 5 = 100, 95, 90, 85, 70
# average = 88

# Bob → top 5 = 100, 95, 90, 80, 75
# average = 88

# If there's a tie, return either student.

# Constraints
# Up to 10^5 score records
# A student can have many scores
# Don't sort all scores globally if you can avoid it.
scores = [
    ("Alice", 90),
    ("Bob", 80),
    ("Alice", 70),
    ("Bob", 100),
    ("Alice", 95),
    ("Bob", 90),
    ("Alice", 85),
    ("Bob", 75),
    ("Alice", 100),
    ("Bob", 95),
]
import heapq

def average(arr):
    return sum(arr)/len(arr)

def highest_top5_average(scores):
    top_5 = {}
    for score in scores:
        student = score[0]
        grade = score[1]
        if student not in top_5:
            top_5[student] = []
        if len(top_5[student]) < 5:
            heapq.heappush(top_5[student], score[1])
        elif grade > top_5[student][0]:
            heapq.heappop(top_5[student])
            heapq.heappush(top_5[student], score[1])
    # calculate average and max
    max_avg = 0
    max_avg_student = ''
    for key, val in top_5.items():
        if average(val) > max_avg:
            max_avg = average(val)
            max_avg_student = key
    return max_avg_student + " with average "+ str(max_avg)

print(highest_top5_average(scores))
                    