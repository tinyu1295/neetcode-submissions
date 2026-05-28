class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        left = list(s)
        curr = 0
        print(left)
        while curr <= len(t)-1:
            if t[curr] in left:
                left.remove(t[curr])
                curr+=1
            else:
                return False
        return True

        