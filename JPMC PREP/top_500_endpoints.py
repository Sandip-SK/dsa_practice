logs = [
    "10.0.0.1 GET /api/users 200",
    "10.0.0.2 GET /api/orders 500",
    "10.0.0.3 GET /api/users 500",
    "10.0.0.4 GET /api/orders 500",
    "10.0.0.5 GET /api/users 200",
    "10.0.0.6 GET /api/orders 500",
]

def top_500_endpoints(logs):
    parts = list()
    for log in logs:
        parts.append(log.split())
    # count 500
    res = {}
    for part in parts:
        if part[3] == '500':
            res[part[2]] = res.get(part[2], 0) + 1
    max_count = max(res.values())
    result = []
    for endpoint, count in res.items():
        if count == max_count:
            result.append(endpoint)
    return result

top_500_endpoints(logs=logs)