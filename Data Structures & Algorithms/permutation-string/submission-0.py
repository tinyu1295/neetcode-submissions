class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        s1_count = [0] * 26
        win_count = [0] * 26
        ordA = ord('a')

        for s in s1:
            s1_count[ord(s)-ordA] += 1
        
        for i in range(len(s1)):
            win_count[ord(s2[i])-ordA] += 1
        
        print(s1_count, win_count)
        if s1_count == win_count:
            return True
        
        for i in range(len(s1), len(s2)):
            win_count[ord(s2[i])-ordA] += 1
            win_count[ord(s2[i-len(s1)])-ordA] -= 1
            if win_count == s1_count: return True
        
        return False
        



