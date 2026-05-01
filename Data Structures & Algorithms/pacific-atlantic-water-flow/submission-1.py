class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pac, atl = set(), set()

        def init(row, col, visited, prev):
            if (
                row in range(len(heights)) and
                col in range(len(heights[0])) and
                (row,col) not in visited and
                heights[row][col]>=prev
            ):
                visited.add((row,col))
                direc=[[0,1],[0,-1],[1,0],[-1,0]]
                for dr, dc in direc:
                    init(row+dr,col+dc, visited, heights[row][col])

        for row in range(len(heights)):
            init(row, 0, pac, heights[row][0])
            init(row, len(heights[0])-1, atl, heights[row][len(heights[0])-1])
        
        for col in range(len(heights[0])):
            init(0, col, pac, heights[0][col])
            init(len(heights)-1, col, atl, heights[len(heights)-1][col])
        
        res=[]
        for i in range(len(heights)):
            for j in range(len(heights[0])):
                if (i,j) in pac and (i,j) in atl:
                    res.append([i,j])
        return res