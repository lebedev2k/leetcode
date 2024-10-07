import string

def numberOfSpecialChars(word: str) -> int:
    chars = set(word)
    c1 = set(string.ascii_lowercase) & chars
    c2 = set(map(str.lower, set(string.ascii_uppercase) & chars))
    return len(c1 & c2)


assert numberOfSpecialChars("aaAbcBC") == 3

            