def capitalizeTitle(title: str) -> str:
    a = title.split()
    res = []
    for word in a:
        if len(word) < 3:
            res.append(word.lower())
        else:
            res.append(word.capitalize())
    return ' '.join(res)

print(capitalizeTitle("capiTalIze tHe titLe"))