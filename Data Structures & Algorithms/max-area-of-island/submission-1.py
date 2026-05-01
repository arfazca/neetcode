class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        V, area = set(), 0
        def init(r:int, c:int):
            if (
                r not in range(len(grid)) or
                c not in range(len(grid[0])) or
                grid[r][c]==0 or
                (r,c) in V
            ):
                return 0
            
            V.add((r,c))
            return 1 + init(r+0,c+1) + init(r+0,c-1) + init(r+1,c+0) + init(r-1,c+0)

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                area=max(area,init(r,c))
        
        return area
