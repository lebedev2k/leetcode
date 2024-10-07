from typing import List

def addToArrayForm(num: List[int], k: int) -> List[int]:
    ak = list(map(int, str(k)))
    if len(ak) < len(num):
        num, ak = ak, num
    for i in range(len(num)-1, -1, -1):
        num[i], carry = num[i]+ak[i], 0
        if num[i] > 9:
            num[i], carry = num[i]%10, 1
        if carry:
            ak.insert(0, carry)
    return num

        
            
    # return list(
    #             map(int,
    #                 list(str(int(''.join(list(map(str,num))))+k))
    #             )
    #         )

assert addToArrayForm([1, 2, 0, 0], 34) == [1, 2, 3, 4]
assert addToArrayForm([2, 7, 4], 181) == [4, 5, 5]
assert addToArrayForm([2, 1, 5], 806) == [1, 0, 2, 1]
