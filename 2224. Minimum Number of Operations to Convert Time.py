def convertTime(current: str, correct: str) -> int:
    h, m = map(int, current.split(':'))
    m_start = h*60+m
    h, m = map(int, correct.split(':'))
    m_target = h*60+m
    ops = 0
    while m_start != m_target:
        if m_start+60 <= m_target:
            m_start += 60
        elif m_start+15 <= m_target:
            m_start += 15
        elif m_start+5 <= m_target:
            m_start += 5
        elif m_start+1 <= m_target:
            m_start += 1
        ops += 1
    
    return ops
        


assert convertTime("02:30", "04:35") == 3
assert convertTime("11:00", "11:01") == 1
