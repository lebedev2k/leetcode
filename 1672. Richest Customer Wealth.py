def maximumWealth(accounts: list[list[int]]) -> int:
    max_wealth = 0
    for customer_wealth in accounts:
        max_wealth = max(max_wealth, sum(customer_wealth))
    return max_wealth
    

assert maximumWealth([[1,2,3],[3,2,1]]) == 6
assert maximumWealth([[1,5],[7,3],[3,5]]) == 10
assert maximumWealth([[2,8,7],[7,1,3],[1,9,5]]) == 17