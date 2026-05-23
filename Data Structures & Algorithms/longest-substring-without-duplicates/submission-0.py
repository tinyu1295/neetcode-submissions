class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        charSet = list()
        L, totalLen = 0, 0
        currLen = 0
        
        for R in range(len(s)):
            while s[R] in charSet:
                currLen -= 1
                charSet.remove(s[L])
                L+=1
            currLen += 1
            totalLen = max(currLen, totalLen)
            charSet.append(s[R])
        return(totalLen)

        