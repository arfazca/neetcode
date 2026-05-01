class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if not n: return True
        sj, vs = {i:[] for i in range(n)}, set()
        for a, b in edges:
            sj[a].append(b)
            sj[b].append(a)
        def init(c:int, pv:int) -> bool:
            if c in vs: return False
            vs.add(c)
            for p in sj[c]:
                if p==pv: continue
                if not init(p,c): return False
            return True

        return init(0,-1) and n==len(vs)