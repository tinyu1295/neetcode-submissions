class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded=""
        for word in strs:
            encoded+= str(len(word))+"#"+word
        return encoded
    def decode(self, s: str) -> List[str]:

        decoded = []
        left=0
        while left < len(s):
            # find len
            i=left
            while s[i]!="#":
                i+=1
            currLen = int(s[left:i])
            print(currLen)

            # find word

            word = s[i+1:i+1+currLen]
            decoded.append(word)
            left = i+1+currLen

        return decoded