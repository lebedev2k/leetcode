def makeFancyString(s: str) -> str:
    counter = 0
    last_c = ''
    res = ''
    for c in s:
        if last_c == c:
            if counter == 2:
                continue
            counter += 1
        else:
            counter = 1
        last_c = c
        res += c

    return res
            

assert makeFancyString("leeetcode") == "leetcode"
assert makeFancyString("aaabaaaa") == "aabaa"
assert makeFancyString("aab") == "aab"
