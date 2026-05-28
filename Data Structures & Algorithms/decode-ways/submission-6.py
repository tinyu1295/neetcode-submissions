class Solution:
    def numDecodings(self, s: str) -> int:
        if not s or len(s)<3 and "0" == s[0]:
            return 0

        track1 = 1
        track2 = 1

        for i in range(1, len(s)):
            curr = 0

            if s[i] != "0":
                curr += track1
            t = int(s[i-1:i+1])
            if 9<t<27:
                curr += track2
            
            track1 = track2
            track2 = curr

        return track2
