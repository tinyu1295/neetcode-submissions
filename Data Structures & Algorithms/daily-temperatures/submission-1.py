class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        ans = [0] * n

        for i in range(n - 2, -1, -1):
            j = i + 1

            while j < n:
                if temperatures[j] > temperatures[i]:
                    ans[i] = j - i
                    break
                elif ans[j] == 0:
                    break
                else:
                    j += ans[j]

        return ans