class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        curr_permute = []
        n = len(nums)

        def dfs():
            if len(curr_permute) == n:
                res.append(curr_permute.copy())
                return
            
            for x in nums:
                if x not in curr_permute:
                    curr_permute.append(x)
                    dfs()
                    curr_permute.pop()

        dfs()      
        
        return res