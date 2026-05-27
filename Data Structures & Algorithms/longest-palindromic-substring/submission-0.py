class Solution:
    def longestPalindrome(self, s: str) -> str:
        # "ababd"

        res = ""
        maxLen = 0

        for i in range(len(s)):
            # odd palindrome
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                window = r - l + 1
                # print(s[l:r+1], window, maxLen)
                if window > maxLen:
                    res = s[l:r+1]
                    maxLen = window
                l -= 1
                r += 1

            # even palindrome
            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                window = r - l + 1
                if window > maxLen:
                    res = s[l:r+1]
                    maxLen = window
                l -= 1
                r += 1
        
        return(res)