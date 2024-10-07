def squareIsWhite(coordinates: str) -> bool:
    col = "abcdefgh".index(coordinates[0])+1
    row = int(coordinates[1])
    if row % 2 == 0:
        if col % 2 == 0:
            return False
        else:
            return True
    else:
        if col % 2 == 0:
            return True
        else:
            return False
                                
assert squareIsWhite("a1") == False
assert squareIsWhite("h3") == True
assert squareIsWhite("c7") == False