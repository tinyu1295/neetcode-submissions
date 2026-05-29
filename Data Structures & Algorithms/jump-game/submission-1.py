class Solution:
    def canJump(self, nums: List[int]) -> bool:
        goals = len(nums) - 1
        for i in range(len(nums)-1, -1, -1):
            if i + nums[i] >= goals:
                goals = i

        return True if goals == 0 else False
    
            