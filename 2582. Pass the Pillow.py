def passThePillow(n: int, time: int) ->int:
    num = 1
    direction = 1
    while time:
        if direction>0:
            num += 1
        else:
            num -= 1
        if num == n or num == 1:
            direction *= -1

        time -= 1
        
    return num


assert passThePillow(4,5) == 2
