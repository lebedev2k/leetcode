def findMinimumOperations(s1: str, s2: str, s3: str) -> int:
    if s1[0]!=s2[0] and s2[0]!=s3[0]: return -1
    n = min(len(s1), len(s2), len(s3))
    i = 0
    while i<n and s1[i]==s2[i]==s3[i]:
        i += 1
    return (len(s1)-i) + (len(s2)-i) + (len(s3)-i)