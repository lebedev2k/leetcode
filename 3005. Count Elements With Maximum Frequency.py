def maxFrequencyElements(nums: list[int]) -> int:
    from collections import Counter
    freqs = Counter(nums).values()
    max_freq = max(freqs)
    return sum(filter(lambda v: v == max_freq, freqs))


def maxFrequencyElements2(nums: list[int]) -> int:    
    from collections import defaultdict
    max_freq = 0
    freqs = defaultdict(int)
    for n in nums:
        freqs[n] += 1
        max_freq = max(max_freq, freqs[n])
    res = 0
    for freq in freqs.values():
        if freq == max_freq:
            res += freq
    
    return res

def maxFrequencyElements3(nums: list[int]) -> int:    
    from collections import defaultdict
    max_freq = 0
    freqs = defaultdict(int)
    for n in nums:
        freqs[n] += 1
        max_freq = max(max_freq, freqs[n])
    return list(freqs.values()).count(max_freq) * max_freq

assert maxFrequencyElements3([1,2,2,3,1,4]) == 4
assert maxFrequencyElements3([1,2,3,4,5]) == 5
