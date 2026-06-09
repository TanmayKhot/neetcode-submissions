class Solution:
    def solve(self, board: List[List[str]]) -> None:
        
        rows = len(board)
        cols = len(board[0])
        queue = deque()

        for r in range(rows):
            for c in range(cols):
                if (r ==0 or r == rows-1 or c == 0 or c==cols-1) and board[r][c] == "O":
                    queue.append((r,c))
                    board[r][c] = "T"

        while queue:
            r,c = queue.popleft()
            for dr,dc in [(1,0), (-1,0), (0,1), (0,-1)]:
                nr = r+dr
                nc = c+dc
                if 0<=nr<rows and 0<=nc<cols and board[nr][nc] == "O":
                    queue.append((nr,nc))
                    board[nr][nc] = "T" 
        
        print(board)

        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O":
                    board[r][c] = "X"
                elif board[r][c] == "T":
                    board[r][c] = "O"

        return







