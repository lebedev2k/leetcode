from typing import List
def construct2DArray(original: List[int], m: int, n: int) -> List[List[int]]:
    if m*n == len(original): 
        return [original[i:i+n] for i in range(0, len(original), n)]
    return []