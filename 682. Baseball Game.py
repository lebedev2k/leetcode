from typing import List

def calPoints(operations: List[str]) -> int:
    scores = []
    for op in operations:
        if op == '+':
            scores.append(scores[-1]+scores[-2])
        elif op == 'D':
            scores.append(scores[-1]*2)
        elif op == 'C':
            scores.pop()
        else:
            scores.append(int(op))
    return sum(scores)


assert calPoints(["5","2","C","D","+"]) == 30
assert calPoints(["5","-2","4","C","D","9","+","+"]) == 27
assert calPoints(["1","C"]) == 0
