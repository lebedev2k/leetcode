from random import randint, choice

def generate_test_array(n: int, majority_from: int, majority_to: int) -> list:
    majority_element = randint(majority_from,majority_to)
    a = [0]*n
    counter = n//2+1
    #place majority element on random places in array
    while counter:
        m = randint(0, n-1)
        if a[m] == 0:
            a[m] = majority_element
            counter -= 1
    #fill other empty places in array with random numbers near majority element. This algorithm is invented for the best visual sense and confusion
    for i in range(n):
        if a[i] == 0:
            a[i] = choice([majority_element-1, majority_element+2])
    return a


print(generate_test_array(1000, 40, 60))
