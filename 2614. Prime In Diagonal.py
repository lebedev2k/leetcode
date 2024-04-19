from typing import List

def diagonalPrime(nums: List[List[int]]) -> int:
    def isprime(num):
        if num==2 or num==3:
            return True
        if num%2==0 or num<2:
            return False
        for n in range(3,int(num**0.5)+1,2):   
            if num%n==0:
                return False   
        return True
    diagonal_nums = set()
    n = len(nums)
    for i in range(n):
        diagonal_nums.add(nums[i][i])
        diagonal_nums.add(nums[i][n-i-1])
    return max([0]+[i for i in diagonal_nums if isprime(i)])
        
        
assert diagonalPrime([[1,2,3],[5,6,7],[9,10,11]]) == 11
assert diagonalPrime([[1,2,3],[5,17,7],[9,11,10]]) == 17
assert diagonalPrime([[1,1,1],[1,1,1],[1,1,1]]) == 0
