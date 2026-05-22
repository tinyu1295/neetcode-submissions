class Solution:
    def climbStairs(self, n: int) -> int:
        a = 0
        b = 1

        for _ in range(0,n):
            b,a = a+b,b
        
        return b