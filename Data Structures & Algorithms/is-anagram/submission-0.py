class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        left = set(s)
        curr = 0
        print(left)
        while curr <= len(t)-1:
            if t[curr] in left:
                curr+=1
            else:
                return False
        return True

        