class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = nums[0]
        currSum = 0
        for index in range(len(nums)):
            currSum = max(0, currSum)
            currSum += nums[index]
            maxSum = max(maxSum, currSum)

        return maxSum