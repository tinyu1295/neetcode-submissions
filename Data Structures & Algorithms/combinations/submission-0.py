class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:

        res = []
        sol = []
        
        def dfs(x):
            if len(sol) == k:
                res.append(sol.copy())
                return
            
            left = x
            need = k - len(sol)
            if left > need:
                dfs(x - 1)
            
            sol.append(x)
            dfs(x-1)
            sol.pop()
        
        dfs(n)
        return res