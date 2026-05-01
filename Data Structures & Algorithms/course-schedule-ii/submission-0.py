class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # a course has 3 possible states:
        # visited   -> c (aka Course) has been added to output
        # visiting  -> c has not been added to output, but added to cycle
        # unvisited -> c not added to either visited or cycle

        prereq = {c:[p for _c, p in prerequisites if _c==c] for c in range(numCourses)}
        res, vis, cyc = [], set(), set()

        def init(c:int) -> bool:
            if c in cyc: return False
            if c in vis: return True

            cyc.add(c)
            for p in prereq[c]:
                if not init(p): return False
            cyc.remove(c)
            vis.add(c)
            res.append(c)
            return True
        for c in range(numCourses):
            if not init(c): return []
        return res