class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        arr.sort(reverse=True)
        arr[1]=arr[0]
        arr[-1]=-1
        return arr
        