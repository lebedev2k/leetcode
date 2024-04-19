def oddString(words: list[str]) -> str:
    from collections import defaultdict
    d = defaultdict(list)
    for i, word in enumerate(words):
        a = '#'.join([str(ord(word[j+1])-ord(word[j])) for j in range(len(word)-1)])
        d[a].append(i)

    for v in d.values():
        if len(v)==1:
            return words[v[0]]
    

assert oddString(["adc","wzy","abc"]) == "abc"
assert oddString(["aaa","bob","ccc","ddd"]) == "bob"
assert oddString(["abm","bcn","alm"]) == "alm"
