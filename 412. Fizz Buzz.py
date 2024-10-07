from typing import List

def fizzBuzz2(n: int) -> List[str]:
    return ["FizzBuzz" if (i % 15 == 0) else "Fizz" if (i % 3 == 0) else "Buzz" if (i % 5 == 0) else str(i) for i in range(1, n+1)]

def fizzBuzz(n: int) -> List[str]:
    result = [str(i) for i in range(1, n + 1)]
    for i in range(3, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            result[i - 1] = "FizzBuzz"
        elif i % 3 == 0:
            result[i - 1] = "Fizz"
        elif i % 5 == 0:
            result[i - 1] = "Buzz"
                                                                
    return result


assert fizzBuzz(3) == ['1', '2', 'Fizz']
assert fizzBuzz(5) == ['1', '2', 'Fizz', '4', 'Buzz']
assert fizzBuzz(15) == ['1', '2', 'Fizz', '4', 'Buzz', 'Fizz', '7', '8', 'Fizz', 'Buzz', '11', 'Fizz', '13', '14', 'FizzBuzz']

    