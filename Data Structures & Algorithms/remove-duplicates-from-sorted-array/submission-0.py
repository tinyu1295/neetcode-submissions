class Solution:
    def removeDuplicates(self, nums):
        unique = sorted(set(nums))
        print(unique)
        print(nums[:len(unique)])
        e = unique
        print(e)
        nums[:len(unique)] = unique
        return len(unique)
        