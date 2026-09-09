def first_duplicate_1(arr):
    c_arr = {}

    for i in arr:
        if i not in c_arr:
            c_arr[i] = 1
        else:
            return i

    return None

def first_duplicate(arr):
    seen = set()

    for i in arr:
        if i in seen:
            return i
        seen.add(i)

    return None

