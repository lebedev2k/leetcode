from typing import List
def sortJumbled(mapping: List[int], nums: List[int]) -> List[int]:
    def comparator(x):
        r = ''
        for n in str(x[0]):
            r += mapping[int(n)]
        return (int(r),x[1])
    
    mapping = list(map(str, mapping))
    v = [(x,i) for i,x in enumerate(nums)]
    v.sort(key=comparator)
    return [item[0] for item in v]

assert sortJumbled([8,9,4,0,2,1,3,5,7,6], [991,338,38]) == [338,38,991]
assert sortJumbled([0,1,2,3,4,5,6,7,8,9], [789,456,123]) == [123,456,789]