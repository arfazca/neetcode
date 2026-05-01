class Solution:
    def DFS (self, r: int, c: int):
        if (r not in range(self.rows) or c not in range(self.cols) or self.grid[r][c]=='0' or (r,c) in self.storage):
            return
        self.storage.add((r,c))
        sy=[[0,1],[0,-1],[1,0],[-1,0]]
        for dr, dc in sy:
            self.DFS(r+dr, c+dc)
    def numIslands(self, grid: List[List[str]]) -> int:
        self.grid = grid
        if not grid or not grid[0]: return 0
        self.storage, self.islands = set(), 0
        self.rows, self.cols = len(grid), len(grid[0])
        for i in range(self.rows):
            for j in range(self.cols):
                if (i, j) not in self.storage and grid[i][j]!='0':
                    self.islands+=1
                    self.DFS(i, j)
        return self.islands