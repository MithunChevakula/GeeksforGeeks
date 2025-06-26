#User function Template for python3

class Solution:
    def nQueen(self, n):
        # code here
        def isSafe(board, n, r, c):
            dupRow = r
            dupCol = c

            while (r >= 0 and c >= 0):
                # print(r, c, "1")
                if board[r][c] == 'Q':
                    return False
                r -= 1
                c -= 1

            r = dupRow
            c = dupCol

            while (c >= 0):
                # print(r, c, "2")

                if board[r][c] == 'Q':
                    return False
                c -= 1

            r = dupRow
            c = dupCol
            while (r < n and c >= 0):
                # print(r, c, "3")

                if board[r][c] == 'Q':
                    return False
                r += 1
                c -= 1

            return True

        def recursion(ans, n, board, col):

            if col == n:
                dupBoard = [0 for i in range(n)]
                for i in range(n):
                    for j in range(n):
                        if board[i][j]=='Q':
                            dupBoard[j]=i+1

                ans.append(dupBoard)
                return


            for row in range(n):
                if isSafe(board, n, row, col):
                    # print(row, col)
                    board[row][col] = 'Q'
                    recursion(ans, n, board, col+1)
                    board[row][col] = '.'

            return

 

        ans = []

        # s=""
        # for i in range(n):
        #     s+='.'

        board = [['.' for i in range(n)] for j in range(n)]
        recursion(ans, n, board, 0)
        return ans