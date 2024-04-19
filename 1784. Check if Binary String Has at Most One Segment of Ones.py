def checkOnesSegment(s: str) -> bool:
    return '01' not in s


assert checkOnesSegment("1001") == False
assert checkOnesSegment("110") == True
