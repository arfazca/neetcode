class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        q, s = deque(), set()
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c]==0:
                    q.append((r,c))
                    s.add((r,c))
        
        def init (r:int, c:int, t:int):
            if (
                r in range(len(grid)) and
                c in range(len(grid[0])) and
                (r,c) not in s and
                grid[r][c]!=-1
            ):
                grid[r][c]=t
                q.append((r,c))
                s.add((r,c))

        t = 1
        direc=[[0,1],[0,-1],[1,0],[-1,0]]
        while q:
            for i in range(len(q)):
                r, c = q.popleft()
                for dr, dc in direc:
                    init(r+dr, c+dc, t)
            t+=1

