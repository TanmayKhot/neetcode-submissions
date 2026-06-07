class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        rows = len(heights)
        cols = len(heights[0])

        pac = set()
        atl = set()

        def dfs(r, c, visited, prev_value):

            if 0<=r<rows and 0<=c<cols and (r,c) not in visited and heights[r][c] >= prev_value:
                visited.add((r,c))
                dfs(r+1, c, visited, heights[r][c])
                dfs(r-1, c, visited, heights[r][c])
                dfs(r, c-1, visited, heights[r][c])
                dfs(r,c+1, visited, heights[r][c])

            return

        for c in range(cols):
            dfs(0, c, pac, heights[0][c])
            dfs(rows-1, c, atl, heights[rows-1][c])
        
        for r in range(rows):
            dfs(r, 0, pac, heights[r][0])
            dfs(r, cols-1, atl, heights[r][cols-1])

        res = []
        for r in range(rows):
            for c in range(cols):
                if (r,c) in atl and (r,c) in pac:
                    res.append((r,c))

        return res



