class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        conn = {i:[] for i in range(n) }
        visited = set()
        components = 0

        for node1, node2 in edges:
            conn[node1].append(node2)
        print(conn)

        def dfs(node):
            visited.add(node)
            for nei in conn[node]:
                if nei not in visited:
                    dfs(nei)
            

        for node in range(n):
            if node not in visited:
                dfs(node)
                components += 1
        
        return components

