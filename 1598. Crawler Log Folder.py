from typing import List
def minOperations(logs: List[str]) -> int:
    cnt = 0
    for op in logs:
        if op == '../':
            cnt -= 1 if cnt > 0 else 0
        elif op != './':
            cnt += 1
    return cnt


assert minOperations(["d1/","d2/","../","d21/","./"]) == 2
assert minOperations(["d1/","d2/","./","d3/","../","d31/"]) == 3
assert minOperations(["d1/","../","../","../"]) == 0
assert minOperations(["fl6/","nz1/","../","./"]) == 1