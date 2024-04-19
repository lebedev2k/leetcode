def isFascinating(n: int) -> bool:
    result_number = str(n)+str(2*n)+str(3*n)
    print(result_number)
    print(set(result_number))
    print(list(set(result_number) & set('123456789')))
    return len(set(result_number))== len(result_number) and len(list(set(result_number) & set('123456789'))) == 9

assert isFascinating(783) == False
assert isFascinating(192) == True
assert isFascinating(100) == False
    