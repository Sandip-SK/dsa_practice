# You're given CPU utilization measurements for a server:
# cpu = [20, 30, 40, 95, 96, 97, 50, 40, 92, 94]


# We consider the server overloaded if CPU is above 90% for 3 consecutive measurements.
# For the example above:
# 95 → 96 → 97

# means the server was overloaded.
# Write a function:
# def is_overloaded(cpu):    ...


# that returns:
# True

# if there are 3 consecutive measurements above 90%, otherwise:
# False

# Examples
# [20, 50, 91, 92, 93] → True

# [91, 92, 50, 93, 94] → False

# [95, 96, 97, 98] → True

# [] → False

# Interview constraint
# Try to solve this in:
# O(n) time and O(1) extra space.

def is_overloaded(cpu):
    streak = 0
    for load in cpu:
        if load > 90:
            streak += 1
            if streak==3:
                return True
        else:
            streak = 0
    return False