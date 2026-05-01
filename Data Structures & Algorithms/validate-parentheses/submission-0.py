class Solution:
    def isValid(self, s: str) -> bool:
        m={")":"(","]":"[","}":"{"}
        ss=[]
        for c in s: 
            if c not in m:
                ss.append(c)
                continue
            if not ss or ss[-1]!=m[c]:
                return False
            ss.pop()
        return not ss