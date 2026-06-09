class Solution:
    def solve(self, board: List[List[str]]) -> None:
        
        rows = len(board)
        cols = len(board[0])
        queue = deque()
        visited = set()

        for r in range(rows):
            if board[r][0] == "O":
                queue.append((r,0))
                visited.add((r,0))
            elif board[r][cols-1] == "O":
                queue.append((r,cols-1))
                visited.add((r,cols-1))

        for c in range(cols):
            if board[0][c] == "O":
                queue.append((0,c))
                visited.add((0,c))
            elif board[rows-1][c] == "O":
                queue.append((rows-1,c))
                visited.add((rows-1,c))
        
        
        while queue:
            r,c = queue.popleft()
            for dr,dc in [(1,0), (-1,0), (0,1), (0,-1)]:
                nr = r+dr
                nc = c+dc
                if 0<=nr<rows and 0<=nc<cols and (nr,nc) not in visited and board[nr][nc] == "O":
                    queue.append((nr,nc))
                    visited.add((nr,nc))
        
        for r in range(1,rows-1):
            for c in range(1,cols-1):
                if (r,c) not in visited:
                    board[r][c] = "X"

        return







