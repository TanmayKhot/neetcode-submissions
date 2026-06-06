class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        def bfs(arr, start, rows, cols):

            queue = deque([start])
            visited = {(start)}

            while queue:
                r,c = queue.popleft()
                for dr,dc in [(1,0), (-1,0), (0,-1), (0,1)]:
                    nr = r+dr
                    nc = c+dc

                    while 0<=nr<rows and 0<=nc<cols and arr[nr][nc] == "1" and arr[nr][nc] not in visited:

                        visited.add((nr,nc))
                        queue.append((nr,nc))
                        arr[nr][nc] = "-1"
        
        rows = len(grid)
        cols = len(grid[0])
        res = 0

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "1":
                    bfs(grid, (i,j), rows, cols)
                    print(grid)
                    res += 1
        
        return res



