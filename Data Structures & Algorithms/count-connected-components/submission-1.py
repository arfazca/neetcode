class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        par1 = [i for i in range(len(edges)+1)]
        rank2 = [1] * (len(edges)+1)
        par = [i for i in range(n)]
        rank = [1] * n
        print(par, "->", rank)
        print(par1, "->", rank2)
        def find(n):
            while par[n] != par[par[n]]:
                par[par[n]] = par[par[par[n]]]
                par[n] = par[par[n]]
            return par[n]
        # def find(n):
        #     res = n
        #     while res != par[res]:
        #         par[res] = par[par[res]]
        #         res = par[res]
        #     return res
        
        def union(n1, n2):
            p1, p2 = find(n1), find(n2)
            
            if rank[p1]<rank[p2]:
                par[p1] = p2
                rank[p2]+=rank[p1]
            else:
                par[p2] = p1
                rank[p1] += rank[p2]
            return 1
        
        res = n
        for n1, n2 in edges:
            res -= union(n1,n2)
        return res