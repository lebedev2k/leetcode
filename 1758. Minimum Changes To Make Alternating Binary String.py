def minOperations(s: str) -> int:
    cnt0 = 0
    cnt1 = 0
    for i in range(0,len(s),2):
        if s[i] != '0':
            cnt0 += 1
        else:
            cnt1 += 1            
    for i in range(1,len(s),2):
        if s[i] != '1':
            cnt0 += 1
        else:
            cnt1 += 1
        
    return min(cnt0,cnt1)
                
    # zeros = s.count('0')
    # ones   = len(s) - zeros
    # return len(s)//2 - min(zeros,ones)
    # if abs(zeros-ones) > 1:
    #     if  len(s) % 2 == 0:
    #         return len(s)//2 - zeros if ones > zeros else len(s)//2 - ones
    # else: return 0


assert minOperations("0100") == 1
assert minOperations("10") == 0
assert minOperations("1111") == 2
assert minOperations("111000") == 2 # "101010"
