class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        unique = set(nums)
        if val in nums:
            del unique[val]
        print(unique)

        