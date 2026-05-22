class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        wordDic = {}
        result = []
        for word in strs:
            key = "".join(sorted(word))
            if key not in wordDic:
                wordDic[key] = [word]
            else:
                wordDic[key].append(word)
            
        for key, val in wordDic.items():
            result.append(val)
        return result

        
        