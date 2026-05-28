class Solution:
    def rob(self, nums: List[int]) -> int:
        def robHelper(start, end):
            rob1, rob2 = 0, 0
            for i in range(start, end):
                temp = max(nums[i] + rob1, rob2)
                rob1 = rob2
                rob2 = temp
            return rob2

        return max(robHelper(0, len(nums) - 1), robHelper(1, len(nums)))

        