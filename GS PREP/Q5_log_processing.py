logs = [
    (1, "payment", 200),
    (2, "payment", 500),
    (3, "auth", 200),
    (4, "payment", 500),
    (5, "auth", 500),
    (6, "payment", 200),
]

logs2 = [
    (10, "api", 200),
    (11, "api", 503),
    (12, "db", 500),
    (13, "api", 502),
    (14, "db", 500),
    (15, "auth", 404),
    (16, "db", 503),
]

def count_5xx_errors(logs):
    count_500 = {}

    for timestamp, service, status_code in logs:
        if 500 <= status_code <= 599:
            count_500[service] = count_500.get(service, 0) + 1

    return count_500

def highest_error_service(logs):
    counts = {}

    for timestamp, service, status_code in logs:
        if 500 <= status_code <= 599:
            counts[service] = counts.get(service, 0) + 1

    max_service = None
    max_count = 0

    for service, count in counts.items():
        if count > max_count:
            max_count = count
            max_service = service

    return max_service