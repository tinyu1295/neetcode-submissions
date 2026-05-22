class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        curr = 0
        while len(arr)> curr+1:
            arr[curr] = max(arr[curr+1:])
            curr+=1
        arr[curr] = -1
        return arr
        