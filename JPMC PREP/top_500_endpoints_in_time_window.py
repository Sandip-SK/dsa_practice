from collections import deque

logs = [
    (100, "/api/users", 500),
    (120, "/api/orders", 500),
    (200, "/api/users", 500),
    (350, "/api/orders", 500),
]

def top_500_endpoints(logs):
    window = deque()
    counts = {}

    for timestamp, endpoint, status in logs:

        if status == 500:
            # Add current event
            window.append((timestamp, endpoint))
            counts[endpoint] = counts.get(endpoint, 0) + 1

            # Remove events older than 5 minutes
            while window and window[0][0] < timestamp - 300:
                old_timestamp, old_endpoint = window.popleft()
                counts[old_endpoint] -= 1

                if counts[old_endpoint] == 0:
                    del counts[old_endpoint]
    max_count = max(counts.values(), default=0)
    result = [endpoint for endpoint, count in counts.items() if count == max_count]
    return result