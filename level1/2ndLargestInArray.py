def sec_max(arr):
    m1,m2=arr[0], int()
    for i in arr:
        if i>m1:
            m2 = m1
            m1 = i
        elif i<m1 and i>m2:
            m2=i
    return m2