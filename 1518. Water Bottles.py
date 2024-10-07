def numWaterBottles(numBottles: int, numExchange: int) -> int:
    drink_bottles = numBottles
    full_bottles, empty_bottles = divmod(numBottles, numExchange)
    while full_bottles:
        drink_bottles += full_bottles
        full_bottles, empty_bottles = divmod(full_bottles+empty_bottles, numExchange)
    return drink_bottles

assert numWaterBottles(9, 3) == 13
assert numWaterBottles(15, 4) == 19