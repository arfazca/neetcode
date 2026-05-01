class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if not board or not board[0]: return False
        V = set()

        def init(r:int,c:int,i:int):
            if (
                r in range(len(board)) and
                c in range(len(board[0])) and
                (r,c) not in V and
                board[r][c]==word[i]
            ):
                if (i==(len(word)-1)): 
                    return True
                V.add((r,c))
                direc=[[1,0],[-1,0],[0,1],[0,-1]]
                for dr,dc in direc:
                    if init(r+dr,c+dc,i+1):
                        return True
                V.remove((r,c))
                return False
        for r in range(len(board)):
            for c in range(len(board[0])):
                if init(r,c,0): 
                    return True
        return False
