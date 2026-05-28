class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = []
        for i in range(len(temperatures)):
            r = i
            count = 0
            while r < len(temperatures):
                if temperatures[i] < temperatures[r]:
                    result.append(count)
                    break
                r += 1
                count += 1
            if r >= len(temperatures):
                result.append(0)
        
        return(result)

        