from collections import deque
from typing import List

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        visited = [False] * n
        province = 0

        def dfs(city):
            visited[city] = True
            for nei in range(n):
                if isConnected[city][nei] == 1 and not visited[nei]:
                    dfs(nei)

        
        for city in range(n):
            if not visited[city]:
                dfs(city)
                province += 1

        return province