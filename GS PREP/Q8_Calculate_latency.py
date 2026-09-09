# You're given application logs:

# logs = [
#     ("api", 200, 120),
#     ("api", 500, 300),
#     ("api", 200, 150),
#     ("payment", 200, 500),
#     ("payment", 503, 800),
#     ("payment", 200, 600),
#     ("auth", 200, 100),
# ]

# Each record is:

# (service, status_code, latency_ms)

# We want to find the service whose average latency is highest.

# For the example:

# api:
# (120 + 300 + 150) / 3 = 190 ms

# payment:
# (500 + 800 + 600) / 3 = 633.33 ms

# auth:
# 100 / 1 = 100 ms

# Expected:

# payment
# Requirements
# Up to 1 million logs
# Multiple services
# Logs can arrive in any order
# Don't store all logs in memory
# O(n) time

logs = [
    ("api", 200, 120),
    ("api", 500, 300),
    ("api", 200, 150),
    ("payment", 200, 500),
    ("payment", 503, 800),
    ("payment", 200, 600),
    ("auth", 200, 100),
]

def highest_avg_latency(logs):
    avg_latency = {}
    for log in logs:
        if log[0] in avg_latency:
            avg_latency[log[0]]["latency_sum"] += log[2]
            avg_latency[log[0]]["count"] += 1
        else:
            avg_latency[log[0]] = {}
            avg_latency[log[0]]["latency_sum"] = log[2]
            avg_latency[log[0]]["count"] = 1
    highest_avg_latency = 0
    highest_avg_latency_service = ''
    for service in avg_latency:
        avg_latency_val = avg_latency[service]["latency_sum"]/avg_latency[service]["count"]
        if avg_latency_val > highest_avg_latency:
            highest_avg_latency = avg_latency_val
            highest_avg_latency_service = service
    return highest_avg_latency_service

print(highest_avg_latency(logs))