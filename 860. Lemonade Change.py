from typing import List

def lemonadeChange(bills: List[int]) -> bool:
    bill5, bill10 = 0, 0
    for b in bills:
        if b == 5:
            bill5 += 1
        elif b == 10:
            if bill5 == 0: return False
            bill5 -= 1
            bill10 += 1
        elif b == 20:
            if bill10 > 0 and bill5 > 0:
                bill5 -= 1
                bill10 -= 1
            elif bill5 > 2:
                bill5 -= 3
            else: return False
    return True   


print(lemonadeChange([5,5,5,10,20]))
print(lemonadeChange([5,5,10,10,20]))