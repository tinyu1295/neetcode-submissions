class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        wordDic = defaultdict(list)
        result = []
        for word in strs:
            key = "".join(sorted(word))
            wordDic[key].append(word)
        return list(wordDic.values())