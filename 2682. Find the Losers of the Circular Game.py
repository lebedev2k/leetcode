from typing import List
def circularGameLosers( n: int, k: int) -> List[int]:
    passed = set()   
    all = set([i for i in range(1, n+1)])
    current_num = 1
    i = 1
    while True:
        passed.add(current_num)            
        current_num = n if (current_num + i*k)%n == 0 else (current_num + i*k)%n
        if current_num in passed:
            break
        i += 1
    return sorted(all-passed)


assert circularGameLosers(2, 1) == []
assert circularGameLosers(5, 2) == [4,5]
assert circularGameLosers(4, 4) == [2,3,4]