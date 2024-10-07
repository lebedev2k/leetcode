def compareVersion(version1: str, version2: str) -> int:
    revisions1 = list(map(int, version1.split('.')))
    revisions2 = list(map(int, version2.split('.')))
    n1 = len(revisions1)
    n2 = len(revisions2)
    if n1 > n2:
        revisions2 += [0] * (n1 - n2)
    elif n2 > n1:
        revisions1 += [0] * (n2 - n1)
    
    # from itertools import zip_longest
    # zip_longest(revisions1, revisions2, fillvalue=0)
    
    for i in range(len(revisions1)):
        if revisions1[i] > revisions2[i]:
            return 1
        elif revisions1[i] < revisions2[i]:
            return -1
    return 0
    

assert compareVersion("1", "1.1") == -1
assert compareVersion("1.01", "1.001") == 0
assert compareVersion("1.0", "1.0.0") == 0
assert compareVersion("0.1", "1.1") == -1