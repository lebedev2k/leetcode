def findLatestTime(s: str) -> str:
    if s[0] == '?':
        if s[1] != '?' and int(s[1])>1:
            res = '0'
        else:
            res = '1'
    else:
        res = s[0]      

    if s[1] == '?':
        if res[0] == '0':
            res += '9:'
        else:
            res += '1:'
    else:
        res += s[1]+':'
    res += '5' if s[3] == '?' else s[3]
    res += '9' if s[4] == '?' else s[4]
    print(res)
    return res


assert findLatestTime("?3:12") == "03:12"
assert findLatestTime("?1:?6") == "11:56"
assert findLatestTime("1?:?4") == "11:54"
assert findLatestTime("0?:5?") == "09:59"