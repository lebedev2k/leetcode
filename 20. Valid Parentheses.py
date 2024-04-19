  
def isValid2(s: str) -> bool:
    brackets_pairs = {
            ']': '[',
            ')': '(',
            '}': '{'
        }
    brackets = []
    for c in s:
        if c in '({[':
            brackets.append(c)
        elif brackets:
            if brackets_pairs[c]==brackets[-1]:
                brackets.pop()
            else:
                return False
        else:
            return False

    return brackets == []    
    
assert isValid("()[]{}") == True
assert isValid("()") == True
assert isValid("(]") == False