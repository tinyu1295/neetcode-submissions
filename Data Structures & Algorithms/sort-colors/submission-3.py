class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        bucket = [0]*len(set(nums))
        print(len(bucket))
        for i in nums:
            bucket[i]+=1
        print(bucket)
        index = 0
        for i in range(0, len(bucket)):
            while bucket[i]:
                bucket[i] -=1
                nums[index] = i
                index+=1
        
        return nums
        

        