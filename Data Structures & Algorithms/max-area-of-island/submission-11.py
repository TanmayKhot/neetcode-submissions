class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        def dfs(grid, r, c):

            rows = len(grid)
            cols = len(grid[0])
            stack = []
            visited = set()
            stack.append((r,c))
            area = 0

            while stack:
                nr, nc = stack.pop()
                grid[nr][nc] = -1
                area += 1
                for dr, dc in [(1,0), (-1,0), (0,1), (0,-1)]:
                    rr = nr+dr
                    cc = nc+dc

                    if 0<=rr<rows and 0<=cc<cols and grid[rr][cc] == 1 and (rr,cc) not in visited:
                        visited.add((rr,cc))
                        stack.append((rr,cc))

            return area
        
        res = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    a = dfs(grid, r, c)
                    res = max(res,a)
        
        return res
