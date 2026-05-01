class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]: return 0
        V, island = set(), 0

        def init(r:int, c:int):
            if (
                r in range(len(grid)) and
                c in range(len(grid[0])) and
                (r,c) not in V and
                grid[r][c]!='0'
            ):
                direc=[[0,1],[0,-1],[1,0],[-1,0]]
                V.add((r,c))
                for dr, dc in direc:
                    init(r+dr, c+dc)

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c]=='1' and (r,c) not in V:
                    island+=1
                    init(r, c)
        return island