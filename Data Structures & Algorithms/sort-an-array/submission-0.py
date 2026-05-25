class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        # [1, 1, 2, 1, 9, 10, 3, 1]
        result = []
        heapq.heapify(nums)
        
        while nums:
            print(len(nums))
            result.append(heapq.heappop(nums))

        return(result)