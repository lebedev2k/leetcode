#https://leetcode.com/problems/two-sum/description/?submissionId=1052456196

def two_sum(nums, target):
    for i in range(0, len(nums) - 1):
        b = target - nums[i]
        for j in range(i + 1, len(nums)):
            if nums[j] == b:
                return [i, j]


def two_sum2(nums, target):
    nums2 = []
    for i in range(0, len(nums)):
        nums2.append((nums[i], i))
    nums = sorted(nums2, key=lambda item: item[0])

    def find_add_num(nums, start_idx, finish_idx, subtarget, first_item):
        if start_idx>finish_idx:
            return []

        if finish_idx - start_idx == 0:
            if nums[start_idx][0] == subtarget and nums[start_idx][1] != first_item[1]:
                return nums[start_idx]
            else:
                return []

        middle_idx = (start_idx + finish_idx) // 2
        if nums[middle_idx][0] >= subtarget:
            return find_add_num(nums, start_idx, middle_idx, subtarget, first_item)
        else:
            return find_add_num(nums, middle_idx+1, finish_idx, subtarget, first_item)

    for item in nums:
        subtarget = target-item[0]
        second_item = find_add_num(nums, 0, len(nums)-1, subtarget, item)
        if second_item:
            return [item[1], second_item[1]]
    return []

print(two_sum2([2, 7, 38, 15, 22], 22))
# print(two_sum([2, 7, 11, 15], 9) == [0,1])
# print(two_sum([3, 2, 4], 6) == [1,2])
# print(two_sum([3, 3], 6) == [0, 1])
