
# For each service, calculate its error rate:

# error rate = number of 5xx requests / total requests

# For the example:

# api:
#     total = 5
#     errors = 2
#     error rate = 40%

# payment:
#     total = 3
#     errors = 2
#     error rate = 66.67%

# Return the service with the highest error rate.
logs = [
    (1, "api", 200),
    (2, "api", 500),
    (3, "api", 200),
    (4, "payment", 500),
    (5, "payment", 500),
    (6, "api", 503),
    (7, "payment", 200),
    (8, "api", 200),
]
def highest_error_rate(logs):
    ser_error = {}
    ser_total = {}
    for rec in logs:
        #update the total and the error
        if rec[1] in ser_total:
            ser_total[rec[1]] += 1
            if rec[2] > 499 and rec[2] < 600:
                if rec[1] in ser_error:
                    ser_error[rec[1]] += 1
                else:
                    ser_error[rec[1]] = 1
        else:
            ser_total[rec[1]] = 1
            if rec[2] > 499 and rec[2] < 600:
                if rec[1] in ser_error:
                    ser_error[rec[1]] += 1
                else:
                    ser_error[rec[1]] = 1
    max_error_rate = 0
    max_err_service = ''
    for i in ser_error:
        error_rate = ser_error[i] / ser_total[i]
        if error_rate > max_error_rate:
            max_error_rate = error_rate
            max_err_service = i
    return max_err_service