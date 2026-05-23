class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [1]*n

        #for prefix
        prefix = 1
        for i in range(n):
            result[i] = prefix
            prefix *= nums[i]
        
        #for suffix
        suffix = 1
        for i in range(n-1, -1, -1):
            result[i] *= suffix
            suffix *= nums[i]
        
        print(result)
        # return result

        return result
                