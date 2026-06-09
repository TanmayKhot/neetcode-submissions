class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        rows = len(grid)
        cols = len(grid[0])
        rotten = deque()
        visited = set()

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    rotten.append((r,c, 0))
                    visited.add((r,c))

        res = 0
        while rotten:
            r,c,l = rotten.popleft()
            res = max(l,res)
            for dr,dc in [(1,0), (-1,0), (0,1), (0,-1)]:
                nr = r+dr
                nc = c+dc
                if 0<=nr<rows and 0<=nc<cols and grid[nr][nc] == 1 and (nr,nc) not in visited:
                    rotten.append((nr,nc,l+1))
                    visited.add((nr,nc))
                    grid[nr][nc] = -1
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    return -1
        
        return res


        
