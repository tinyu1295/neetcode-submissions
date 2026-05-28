class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        nums = sorted([x for x in nums if x != val])
        print(nums)
        return len(nums)

        