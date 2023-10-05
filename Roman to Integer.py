# https://leetcode.com/problems/roman-to-integer/

def romanToInt(s: str) -> int:
    roman_dict = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    result = 0
    last_num = None
    for i in range(len(s) - 1, -1, -1):
        n = roman_dict[s[i]]
        if last_num is None or n >= last_num:
            result += n
        else:
            result -= n
        last_num = n
    return result

assert (romanToInt("MCMXCIV") == 1994)