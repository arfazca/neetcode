class Solution:
    def isValid(self, s: str) -> bool:
        R=[]
        # M={"]":"[","}":"{",")":"("}
        M={
            "(":")",
            "{":"}",
            "[":"]"
        }
        for c in s:
            if c in M:
                R.append(M[c])
            else:
                if R and c != R[-1]: return False
                elif R: R.pop()
                else: return False
        return True
