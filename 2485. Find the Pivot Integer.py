def pivotInteger(n: int) -> int:
    from itertools import accumulate
    a = [i for i in range(n+1)]
    prefix_summ = list(accumulate(a))
    n = len(prefix_summ)
    for i in range(1,n):
        if prefix_summ[i] == prefix_summ[n-1] - prefix_summ[i-1]:
            return a[i]
    return -1


assert pivotInteger(8) == 6
assert pivotInteger(1) == 1
assert pivotInteger(4) == -1