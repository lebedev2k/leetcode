def isPalindrome(s: str) -> bool:
    s = s.lower()
    a = [s[i] for i in range(len(s)) if s[i].isalnum()]
    return a == a[::-1]


assert isPalindrome("A man, a plan, a canal: Panama") == True
assert isPalindrome("race a car") == False
assert isPalindrome(" ") == True