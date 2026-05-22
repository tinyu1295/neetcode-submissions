class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        unique = sorted([x for x in nums if x != val])
        
        print(unique)
        nums[:len(unique)] = unique
        return len(unique)

        