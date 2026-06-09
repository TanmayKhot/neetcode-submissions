class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        
        rows = len(grid)
        cols = len(grid[0])
        INF = 2147483647

        queue = deque()
        visited = set()

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    queue.append((r,c,0))
                    visited.add((r,c))
        
        while queue:
            r,c,l = queue.popleft()

            for dr,dc in [(0,1), (0,-1), (1,0), (-1,0)]:
                nr = r+dr
                nc = c+dc

                if 0<=nr<rows and 0<=nc<cols and (nr,nc) not in visited and grid[nr][nc] != -1:
                    queue.append((nr,nc,l+1))
                    visited.add((nr,nc))
                    grid[nr][nc] = l+1
                   
        
        return