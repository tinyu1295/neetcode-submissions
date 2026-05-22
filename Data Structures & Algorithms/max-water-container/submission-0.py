class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights)-1

        maxWater = 0

        while left<right:

            # maxWater = max()
            width = right-left
            maxWater = max(maxWater, width * min(heights[left],heights[right]))
            if heights[left]<heights[right]:
                left+=1
            elif heights[left]>heights[right]:
                right-=1
            else:
                right-=1
        
        print(maxWater)
        return maxWater
