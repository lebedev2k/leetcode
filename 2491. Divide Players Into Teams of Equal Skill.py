from typing import List

def dividePlayers(skill: List[int]) -> int:
    skill_sum = sum(skill)
    pairs_num = len(skill)//2
    if skill_sum%pairs_num != 0: return -1
    
    equal_sum = skill_sum//pairs_num
    skill.sort()
    a, b = 0, len(skill)-1
    res = 0
    while a < b:
        if skill[a] + skill[b] != equal_sum: return -1
        res += skill[a] * skill[b]
        a += 1
        b -= 1
    return res
        


assert dividePlayers([3,2,5,1,3,4]) == 22
assert dividePlayers([3,4]) == 12
assert dividePlayers([1,1,2,3]) == -1