class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        r = len(grid)
        c = len(grid[0])
        visited = set()
        def helperPath(ROWS, COLS, grid, visited):
            score = 0
            curr = (ROWS,COLS)
            
            print(curr)
            if min(ROWS,COLS)<0 or ROWS==r or COLS==c or curr in visited or grid[ROWS][COLS] == 1:
                return 0
            elif ROWS==3 and COLS==3:
                return 1
            visited.add(curr)

            score += helperPath(ROWS+1, COLS, grid, visited)
            score += helperPath(ROWS-1, COLS, grid, visited)
            score += helperPath(ROWS, COLS+1, grid, visited)
            score += helperPath(ROWS, COLS-1, grid, visited)

            visited.remove(curr)
            print(score)
            return score
        return helperPath(0, 0, grid, visited)
            


        