class Solution:
    def rob(self, nums: List[int]) -> int:

        def robHelper(h):
            rob1, rob2 = 0, 0

            for n in h:
                temp = max(n+rob1, rob2)
                rob1 = rob2
                rob2 = temp
            
            return rob2
        return max(robHelper(nums[:-1]), robHelper(nums[1:]))

        