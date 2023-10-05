def longestCommonPrefix(strs: list[str]) -> str:
    stat = [0] * len(strs)
    prefix = strs[0]
    for i in range(len(strs[0])):
        stat[0] += ord(strs[0][i])
        stop_search = False
        for j in range(1, len(strs)):
            stat[j] += ord(strs[j][i]) if len(strs[j]) > i else 0
            if stat[0] != stat[j]:
                stop_search = True
                break
        if stop_search:
            prefix = strs[0][:i]
            break
    return prefix


assert (longestCommonPrefix(["flower", "flow", "flight"]) == 'fl')
assert (longestCommonPrefix(["dog", "racecar", "car"]) == '')
assert (longestCommonPrefix(["action", "art", "away"]) == 'a')
assert (longestCommonPrefix(["a"]) == 'a')
