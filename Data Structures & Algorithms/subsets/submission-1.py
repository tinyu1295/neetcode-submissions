class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)

        curr_subset = []

        def dfs(i):

            if i >= n:
                res.append(curr_subset.copy())
                return

            # skip
            dfs(i+1)

            # pick
            curr_subset.append(nums[i])
            dfs(i+1)
            curr_subset.pop()
        
        dfs(0)
        
        return res