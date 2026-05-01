class Solution:
    def isValid(self, s: str) -> bool:
        R = []
        M = {
            "(": ")",
            "{": "}",
            "[": "]"
        }
        for c in s:
            if c in M:  # If it's an opening bracket
                R.append(M[c])
            else:  # If it's a closing bracket
                if not R or (R[-1] != c):  # Check if it matches the last opening bracket
                    return False
                R.pop()
        return not R
