def missing_number(arr,n):
    n_sum = n*(n+1)//2
    s = 0
    for i in arr:
        s+=i
    return n_sum - s