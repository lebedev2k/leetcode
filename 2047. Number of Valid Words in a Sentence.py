import string
def countValidWords(sentence: str) -> int:
    cnt = 0
    punctuation =  set("!,.")
    numbers =  set(string.digits)
    letters =  set(string.ascii_lowercase)
    hypens =  "-"
    for word in map(str.strip, sentence.split()):
        set_word = set(word)
        if not set_word.intersection(numbers): #rule 1           
            #rule 2
            n = word.count(hypens)            
            if n > 1:
                continue
            else:
                if n == 1:
                    idx = word.index(hypens)
                    if not (idx>0 and idx<len(word)-1 and word[idx-1] in letters and word[idx+1] in letters):
                        continue
            #rule 3            
            p_chars = set_word.intersection(punctuation)
            if len(p_chars)>1:
                continue
            elif len(p_chars) == 1:
                p_char = p_chars.pop()
                if word.count(p_char)>1:
                    continue
                if word[-1] != p_char:
                    continue
            cnt +=  1                    
                     
    return cnt
        



assert countValidWords("!this  1-s b8d!")   ==  0
assert countValidWords("cat and  dog")  == 3
assert countValidWords("alice and  bob are playing stone-game10")  ==  5


