class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        numSet = set(nums)
        
        def maxConFinder(numSet):
            maxLen = 0
            for i in numSet:
                if i - 1 not in numSet:
                    length = 1
                    while i + length in nums:
                        length += 1
                    maxLen = max(maxLen, length)
            return maxLen
        return maxConFinder(numSet)
            
        
                
