class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        globMax, globMin = nums[0], nums[0]

        currMax, currMin = 0, 0
        totalSum = 0

        for num in nums:
            currMax = max(currMax+num, num)
            currMin = min(currMin+num, num)

            totalSum += num
            globMax = max(currMax, globMax)
            globMin = min(currMin, globMin)

        return max(globMax, totalSum-globMin) if globMax >0 else globMax


        