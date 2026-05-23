class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        maxR = -1

        for i in range(len(arr)-1, -1, -1):
            curr = arr[i]
            arr[i] = maxR
            maxR = max(curr, maxR)
        return arr
        