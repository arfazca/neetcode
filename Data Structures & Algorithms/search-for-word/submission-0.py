class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if not board or not board[0]: return False
        ROWS, COLS = len(board), len(board[0])
        V = set()

        def dfs(r: int, c: int, i: int) -> bool:
            if (
                r in range(ROWS) and
                c in range(COLS) and
                (r, c) not in V and
                board[r][c] == word[i]
            ):
                if i == len(word) - 1: return True

                V.add((r, c))
                direc = [[0,1], [0,-1], [1,0], [-1,0]]
                for dr, dc in direc:
                    if dfs(r + dr, c + dc, i + 1):
                        return True
                V.remove((r, c))
            return False

        for r in range(ROWS):
            for c in range(COLS):
                if dfs(r, c, 0):
                    return True
        return False
