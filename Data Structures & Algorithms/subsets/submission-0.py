class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        currSubset = []
        def dfs(i):
            if i >= len(nums):
                print(currSubset)
                result.append(currSubset.copy())
                return
            
            #skip
            dfs(i+1)

            #pick
            currSubset.append(i+1)
            dfs(i+1)
            currSubset.pop()
        
        dfs(0)
        return(result)