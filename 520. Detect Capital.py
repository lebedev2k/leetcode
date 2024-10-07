def detectCapitalUse(word: str) -> bool:
    cnt_capital = 0
    cnt_lowers = 0
    for c in word:
        if c.isupper():
            cnt_capital += 1
        elif c.islower():
            cnt_lowers += 1
    return cnt_capital == len(word) or cnt_lowers == len(word) or (cnt_capital==1 and word[0].iscapital())