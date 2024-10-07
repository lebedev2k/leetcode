def maximumOddBinaryNumber(s: str) -> str:
    n1 = s.count('1')
    n0 = len(s) - n1
    return ('1'*(n1-1)) + '0'*n0 + '1'


assert maximumOddBinaryNumber("010") == "001"
assert maximumOddBinaryNumber("0101") == "1001"
