class Solution:
    def climbStairs(self, n: int) -> int:
        a = 1
        b = 0

        for p in range(0,n):
            a,b=a+b,a
        return a
        