class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        minPr = float("inf")
        maxPf = 0

        for pr in prices:
            minPr = min(minPr, pr)
            pf = pr - minPr
            maxPf = max(maxPf, pf)
        
        return maxPf