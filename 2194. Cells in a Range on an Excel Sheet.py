def cellsInRange(s: str) -> list[str]:
    letters = []
    res = []
    for i in range(ord(s[0]), ord(s[3])+1):
        for j in range(int(s[1]), int(s[4])+1):
            res.append(chr(i)+str(j))
    return res

assert(cellsInRange("K1:L2")==["K1","K2","L1","L2"])
assert(cellsInRange("A1:F1")==["A1","B1","C1","D1","E1","F1"])
