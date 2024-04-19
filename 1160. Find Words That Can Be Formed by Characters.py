def countCharacters(words: list[str], chars: str) -> int:
    from  collections import Counter    
    res = 0
    for word in words:
        chars_dict = Counter(chars)
        for c in word:
            if c not in chars_dict or chars_dict[c]==0: 
                break
            else:
                chars_dict[c] -= 1
        else:
            res += len(word)
    return res


assert countCharacters(["cat","bt","hat","tree"], "atach") == 6 
assert countCharacters(["hello","world","leetcode"], "welldonehoneyr") == 10 