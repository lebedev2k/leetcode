from random import randint, choice

def generate_test_array(n: int) -> list:
    a = [None]*(2*n+1)
    single_number = randint(-3*10**4, 3*10**4)
    print('Single number=', single_number)
    a[randint(0, 2*n)] = single_number

    counter = n
    while counter>0:
        new_num = randint(-3*10**4, 3*10**4)
        while new_num == single_number:
            new_num = randint(-3 * 10 ** 4, 3 * 10 ** 4)

        place_1 = randint(0, 2*n)
        while a[place_1] is not None:
            place_1 = randint(0, 2*n)
        place_2 = randint(0, 2*n)
        while a[place_2] is not None or place_2 == place_1:
            place_2 = randint(0, 2*n)

        a[place_1] = new_num
        a[place_2] = new_num
        counter -= 1

    return a

def solution(nums: list) -> int:
    num_counter = {}
    for n in nums:
        if n not in num_counter:
            num_counter[n] = 1
        else:
            num_counter[n] += 1
    return list(filter(lambda key: num_counter[key] == 1, num_counter))[0]


a = generate_test_array(500)
print(a)
print('Solution:', solution(a))
