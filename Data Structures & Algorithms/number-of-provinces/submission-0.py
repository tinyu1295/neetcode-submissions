from collections import deque
from typing import List

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        visited = [False] * n
        province = 0

        def bfs(city):
            visited[city] = True
            queue = deque([city])
            while queue:
                city = queue.popleft()
                for nei in range(n):
                    if (isConnected[city][nei] and not visited[nei]):
                        visited[nei] = True
                        queue.append(nei)

        
        for city in range(n):
            if not visited[city]:
                bfs(city)
                province += 1

        return province