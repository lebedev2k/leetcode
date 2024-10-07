from typing import List

def finalPrices(prices: List[int]) -> List[int]:
    for i in range(len(prices)):
        discount = 0
        for j in range(i+1, len(prices)):
            if prices[j]<=prices[i]:
                discount = prices[j]
                break
        prices[i] -= discount
    return prices
        


assert finalPrices([8,4,6,2,3]) == [4,2,4,2,3]
assert finalPrices([1,2,3,4,5]) == [1,2,3,4,5]
assert finalPrices([10,1,1,6]) == [9,0,1,6]
