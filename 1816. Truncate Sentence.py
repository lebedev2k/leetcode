def truncateSentence(self, s: str, k: int) -> str:
    return ' '.join(s.split()[:4])