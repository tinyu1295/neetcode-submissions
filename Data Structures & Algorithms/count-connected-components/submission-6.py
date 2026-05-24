class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        conn = {i:[] for i in range(n)}
        comp = 0
        visited = set()


        for node1, node2 in edges:
            conn[node1].append(node2)
            conn[node2].append(node1)
        
        def bfs(node):
            q = collections.deque()
            q.append(node)
            visited.add(node)

            while q:
                curr = q.popleft()
                for nei in conn[curr]:
                    if nei not in visited:
                        visited.add(nei)
                        q.append(nei)
        
        for node in range(n):
            if node not in visited:
                bfs(node)
                comp += 1
                
        return comp
