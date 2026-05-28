class Solution:
    def rob(self, nums: List[int]) -> int:
        # print("test")
        moneySum = 0
        if len(nums)<3: return sum(nums)

        for idx in range(0,len(nums),2):
            moneySum+=nums[idx]
        return moneySum