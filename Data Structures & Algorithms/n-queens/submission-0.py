class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        cols_to_avoid = set()
        neg_diagonal_to_avoid = set()
        pos_diagonal_to_avoid = set()
        board = [["."] * n for i in range(n)]
        res = []

        def backTrack(r):
            if r == n:
                res.append(["".join(row) for row in board])
                return
            
            for c in range(n):
                if (c in cols_to_avoid or
                    (r-c) in neg_diagonal_to_avoid or
                    (r+c) in pos_diagonal_to_avoid):
                    continue

                cols_to_avoid.add(c)
                neg_diagonal_to_avoid.add(r-c)
                pos_diagonal_to_avoid.add(r+c)

                board[r][c] = "Q"
                backTrack(r + 1)

                cols_to_avoid.remove(c)
                neg_diagonal_to_avoid.remove(r-c)
                pos_diagonal_to_avoid.remove(r+c)

                board[r][c] = "."
        backTrack(0)
        return res

        