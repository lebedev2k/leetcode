def plusOne(digits: list[int]) -> list[int]:
    for i in range(len(digits)-1, -1, -1):
        if digits[i] == 9:
            digits[i] = 0
        else:
            digits[i] += 1
            return digits
    # digits.insert(0,1)
    return [1] + digits


assert(plusOne([1,2,3])==[1,2,4])
assert(plusOne([4,3,2,1])==[4,3,2,2])
assert(plusOne([9])==[1,0])