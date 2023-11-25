from math import factorial

def climbStairs(n: int) -> int:
    n2 = n//2
    n1 = n%2
    ways = 1

    while n2 != 0:
        ways += factorial(n1+n2)/(factorial(n1)*factorial(n2))
        n2 -= 1
        n1 += 2

    return int(ways)

assert(climbStairs(2)==2)
assert(climbStairs(1)==1)
assert(climbStairs(3)==3)
assert(climbStairs(4)==5)
print(climbStairs(2))
