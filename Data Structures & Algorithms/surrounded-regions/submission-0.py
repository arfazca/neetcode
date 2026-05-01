class Solution:
    def solve(self, board: List[List[str]]) -> None:
        def capture (r:str, c:str):
            if (
                r in range(0, len(board)) and
                c in range(0, len(board[0])) and
                board[r][c]=="O"
            ):
                board[r][c]="T"
                direc=[[0,1],[0,-1],[1,0],[-1,0]]
                for dr, dc in direc:
                    capture(r+dr,c+dc)

        for r in range(len(board)):
            for c in range(len(board[0])):
                if (
                    board[r][c]=="O" and
                    (
                        r in [0, len(board)-1] or 
                        c in [0, len(board[0])-1]
                    )
                ):
                    capture(r, c)
        
        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c]=="O": board[r][c]="X"
        
        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c]=="T": board[r][c]="O"