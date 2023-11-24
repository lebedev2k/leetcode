from math import factorial

def climbStairs(n: int) -> int:
    if n == 1:
        return 1

    if n%2 == 1:
        n2 = n//2
        n1 = 1
        ways = factorial(n1 + n2)
    else:
        n2 = n//2
        n1 = 0
        ways = 1
    nfact = factorial(n)
    while n2 != 1:
        n2 -= 1
        n1 += 2
        # ways += factorial(n1+n2)
        ways += nfact/(factorial(n1)*factorial(n2))
    return ways+1

assert(climbStairs(2)==2)
assert(climbStairs(1)==1)
assert(climbStairs(3)==3)
assert(climbStairs(4)==5)
print(climbStairs(2))
