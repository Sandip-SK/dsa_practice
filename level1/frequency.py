def frequency(arr):
    c_arr = {}

    for i in arr:
        if i not in c_arr:
            c_arr[i] = 1
        else:
            c_arr[i] += 1

    return c_arr

print(frequency([1, 2, 2, 3, 1, 2]))