class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        left = list(s)
        
        curr = 0
        while curr <= len(t)-1:
            if t[curr] in left:
                left.remove(t[curr])
                curr+=1
            else:
                return False
        
        return True

        