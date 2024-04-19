def maxLengthBetweenEqualCharacters(s: str) -> int:
    keys_doubles = set()
    char_stat = {}
    for i, c in enumerate(s):
        if c in char_stat:
            char_stat[c].append(i)
            keys_doubles.add(c)
        else:
            char_stat[c] = [i]
            
    
    if not keys_doubles:
        return -1
    
    max_length = 0
    for key in keys_doubles:
        length = max(char_stat[key])-min(char_stat[key])-1
        max_length = max(max_length, length)
    return max_length
    
    
        


assert maxLengthBetweenEqualCharacters("aa") == 0
assert maxLengthBetweenEqualCharacters("abca") == 2
assert maxLengthBetweenEqualCharacters("cbzxy") == -1
