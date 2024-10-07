
def getLucky(s: str, k: int) -> int:
    num = ''.join([str(ord(c)-96) for c in s])
    for _ in range(k):
        num = str(sum(int(c) for c in num))
    return int(num)