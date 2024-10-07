from typing import List
def replaceWords(dictionary: List[str], sentence: str) -> str:
    sentence_words = sentence.split()
    for i in range(len(sentence_words)):
        root = ''
        for word in dictionary:
            if sentence_words[i].startswith(word):
                if not root:
                    root = word
                elif len(word) < len(root):
                    root = word
        if root:
            sentence_words[i] = root
    return ' '.join(sentence_words)


assert replaceWords(["cat","bat","rat"], "the cattle was rattled by the battery") == "the cat was rat by the bat"
assert replaceWords(["a","b","c"], "aadsfasf absbs bbab cadsfafs") == "a a b c"