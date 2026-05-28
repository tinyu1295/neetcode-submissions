class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}

        for idx,num in enumerate(nums):
            dic[num] = idx

        for idx,num in enumerate(nums):
            diff = target - num
            if diff in dic and dic[diff] != idx:
                return([idx, dic[num]])
        return []
