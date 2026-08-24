class Solution:
    def conflict(self, i, j, board, n):

        for r in range(n):
            if board[r][j] == 'Q':
                return True
        r, c = i, j
        while r >= 0 and c >= 0:
            if board[r][c] == 'Q':
                return True
            r -= 1
            c -= 1
        
        r , c = i, j
        while r >= 0 and c <= n-1:
            if board[r][c] == 'Q':
                return True
            r -= 1
            c += 1
        return False
    def backtrack(self, i, n, order, board):
        if i == n:
            order.append(["".join(board[i]) for i in range(n)])
            return

        for j in range(n):
            if not self.conflict(i, j, board, n):
                board[i][j] = 'Q'
                self.backtrack(i+1, n, order, board)
                board[i][j] = '.'

        return
    def solveNQueens(self, n: int) -> List[List[str]]:
        board = [["." for _ in range(n)] for _ in range(n)]
        order = []
        self.backtrack(0, n, order, board)
        return order