from typing import List
def groupAnagrams(strs: List[str]) -> List[List[str]]:
    res = []
    
    for i in range(len(strs)):
        if strs[i] is not None:
            group = [strs[i]]
            a = sorted(list(strs[i]))
            for j in range(i+1, len(strs)):
                if strs[j] is not None and len(strs[i])==len(strs[j]):
                    b = sorted(list(strs[j]))
                    if a==b:
                        group.append(strs[j])
                        strs[j] = None
            res.append(group)
    return res

# print(groupAnagrams(["eat","tea","tan","ate","nat","bat"]))

assert groupAnagrams(["eat","tea","tan","ate","nat","bat"]) == [["bat"],["nat","tan"],["ate","eat","tea"]]
assert groupAnagrams([""]) == [[""]]
assert groupAnagrams(["a"]) == [["a"]]