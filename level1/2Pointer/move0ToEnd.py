def move0ToEnd(arr):
    pos = 0
    for i in range(len(arr)):
        if arr[i] == 0:
            pass
        else:
            arr[i],arr[pos] = arr[pos], arr[i]
            pos += 1
    return arr