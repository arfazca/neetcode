class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap = {i: [] for i in range(numCourses)}
        for crs, pre in prerequisites:
            preMap[crs].append(pre)
        visit = set()

        def init(c:int):
            if c in visit: return False
            if preMap[c]==[]: return True
            visit.add(c)
            for p in preMap[c]:
                if not init(p): return False
            visit.remove(c)
            preMap[c]=[]
            return True
        for c in range(numCourses):
            if not init(c): return False
        return True