class Solution:
    def longestPalindrome(self, s: str) -> str:
        # "ababd"

        self.res = ""
        self.maxLen = 0

        def palindromeFinder(l, r):
            while l >= 0 and r < len(s) and s[l] == s[r]:
                window = r - l + 1
                if window > self.maxLen:
                    self.res = s[l:r+1]
                    self.maxLen = window
                l -= 1
                r += 1

        for i in range(len(s)):
            # odd palindrome
            l, r = i, i
            palindromeFinder(l, r)

            # even palindrome
            l, r = i, i + 1
            palindromeFinder(l, r)
        
        return(self.res)