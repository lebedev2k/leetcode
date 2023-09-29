def check_brackets(s: str) -> bool:
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


print(check_brackets('(]'))