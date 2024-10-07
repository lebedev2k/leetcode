from typing import List
import heapq

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.nums = nums
        self.k = k
        heapq.heapify(self.nums)
        while len(nums)>k:
            heapq.heappop(self.nums)

    def add(self, val: int) -> int:
        heapq.heappush(self.nums, val)
        if len(self.nums)>self.k:
            heapq.heappop(self.nums)
        # return heapq.nsmallest(1, self.nums)[0]
        return self.nums[0]


# Your KthLargest object will be instantiated and called as such:
nums = [4, 5, 8, 2]
 
    
k = 3
kthLargest = KthLargest(k, nums)
print(kthLargest.add(3))
print(kthLargest.add(5))
print(kthLargest.add(10))
print(kthLargest.add(9))
print(kthLargest.add(4))