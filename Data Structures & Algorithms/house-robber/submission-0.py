class Solution:
    def rob(self, nums: List[int]) -> int:
        # print("test")
        sum = 0
        for idx in range(0,len(nums),2):
            sum+=nums[idx]
        return sum