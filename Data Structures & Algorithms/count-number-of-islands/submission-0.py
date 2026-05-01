class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]: return 0
        storage, islands = set(), 0
        rows, cols = len(grid), len(grid[0])
        def DFS (r: int, c: int):
            if (r not in range(rows) or c not in range(cols) or grid[r][c]=='0' or (r,c) in storage):
                return
            storage.add((r,c))
            sy=[[0,1],[0,-1],[1,0],[-1,0]]
            for dr, dc in sy:
                DFS(r+dr, c+dc)
        for i in range(rows):
            for j in range(cols):
                if (i, j) not in storage and grid[i][j]!='0':
                    islands+=1
                    DFS(i, j)
        return islands