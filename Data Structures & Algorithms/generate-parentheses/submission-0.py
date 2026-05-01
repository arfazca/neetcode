class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def DFS (string: str, left: int, right: int):
            if (len(string)==(n*2)):
                res.append(string)
                return
            if left<n:
                DFS(string+'(',left+1,right)
            if right<left:
                DFS(string+')',left,right+1)
        res=[]
        DFS("",0,0)
        return res