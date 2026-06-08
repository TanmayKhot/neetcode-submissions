class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        def dfs(r,c,rows, cols, grid):

            visited = {(r,c)}
            stack = [(r,c)]
            area = 0

            while stack:
                r,c = stack.pop()
                grid[r][c] = -1
                area += 1
                for dr,dc in [(1,0), (-1,0), (0,-1), (0,1)]:
                    nr = r+dr
                    nc = c+dc
                    if 0<=nr<rows and 0<=nc<cols and (nr,nc) not in visited and grid[nr][nc] == 1:
                        visited.add((nr,nc))
                        stack.append((nr,nc))
            
            return area
        
        rows = len(grid)
        cols = len(grid[0]) 
        res = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    area = dfs(r,c,rows,cols, grid)
                    res = max(res,area)
        
        return res
