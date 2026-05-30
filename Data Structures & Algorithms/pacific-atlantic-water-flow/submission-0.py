class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        
        p_que = deque()
        p_seen = set()

        a_que = deque()
        a_seen = set()

        for r in range(ROWS):
            p_que.append((r, 0))
            p_seen.add((r, 0))
        
        for c in range(1, COLS):
            p_que.append((0, c))
            p_seen.add((0, c))
        
        for r in range(ROWS):
            a_que.append((r, COLS-1))
            a_seen.add((r, COLS-1))
        
        for c in range(0, COLS-1):
            a_que.append((ROWS-1, c))
            a_seen.add((ROWS-1, c))
    
        def bfs(queue, seen):
            coordinate = set()
            while queue:
                for _ in range(len(queue)):
                    i, j = queue.popleft()
                    coordinate.add((i, j))
                    for dri, drj in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                        r, c = i + dri, j + drj
                        if 0 <= r < ROWS and 0 <= c < COLS and (r, c) not in seen and heights[r][c] >= heights[i][j]:
                            seen.add((r, c))
                            queue.append((r, c))
                            
            
            return coordinate
        
        p_coord = bfs(p_que, p_seen)
        a_coord = bfs(a_que, a_seen)

        result = p_coord.intersection(a_coord)
        return list(result)

