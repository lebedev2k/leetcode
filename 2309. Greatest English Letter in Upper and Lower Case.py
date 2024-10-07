# def greatestLetter(s: str) -> str:
#     from collections import Counter
#     s = ''.join(set(s)).lower()
#     c = Counter(s)
#     a = [k for k, v in c.items() if v == 2]
#     a.sort(reverse=True)
#     return a[0].upper() if a else "" 
# '''
# class Solution:
#     def greatestLetter(self, s: str) -> str:
#         s = set(s)
#         upper, lower = ord('Z'), ord('z')
#         for i in range(26):
#             if chr(upper - i) in s and chr(lower - i) in s:
#                 return chr(upper - i)
#         return ''
# '''

# assert greatestLetter("lEeTcOdE") == "E"
# assert greatestLetter("arRAzFif") == "R"
# assert greatestLetter("AbCdEfGhIjK") == ""


def greatestLetter(s: str) -> str:
    s1 = set(s)
    res = []
    for i in s1:
        if i.isupper() and i.lower() in s1:
            res.append(i)
    if not res:
        return ""
    
    return max(res)

    # res.sort(reverse=True)
    # return res[0]

print(greatestLetter("lEeTcOdE"))
print(greatestLetter("zOmZAeam"))

