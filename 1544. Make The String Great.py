def makeGood(s: str) -> str:
    if len(s) == 0 or len(s)==1:
        return s
    
    import string
    a = list(zip(string.ascii_lowercase, string.ascii_uppercase))
    b = list(zip(string.ascii_uppercase, string.ascii_lowercase))
    new_string = []
    while True:
        i = 0
        # last = True
        while i < len(s)-1:
            pair = (s[i], s[i+1])
            if pair not in a and pair not in b:
                new_string.append(s[i])
                i += 1 
                # last = True
            else:
                i += 2
                # last = False
        # if last and len(s)>0:
        if i == len(s)-1:
            new_string.append(s[-1])
        if len(s) == len(new_string):
            break
        s = ''.join(new_string)
        new_string = []
    return s
        
    

assert makeGood("RLlr") == ""
assert makeGood("leEeetcode") == "leetcode"
assert makeGood("abBAcC") == ""
assert makeGood("s") == "s"