class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t=="": return ""
        
        S, T = {}, {}
        minRange, minRangeInt = [-1,-1], float("infinity")
        have, need = 0, len(T)  # Initialize need to 0 first
        
        # Build T and set need correctly
        for c in t:
            T[c] = 1 + T.get(c, 0)
        need = sum(T.values())  # Set need as sum of all required counts
        
        # Sliding Window
        R, L = 0, 0 
        while R < len(s):
            S[s[R]] = 1 + S.get(s[R], 0)
            if s[R] in T and S[s[R]] <= T[s[R]]:  # Only increment have when we actually need this char
                have += 1
            
            while have == need:
                if (R-L+1 < minRangeInt):
                    minRange = [L,R]
                    minRangeInt = R-L+1
                S[s[L]] -= 1
                if s[L] in T and S[s[L]] < T[s[L]]:
                    have -= 1
                L += 1
            R += 1
            
        L,R = minRange
        return s[L:R+1] if minRangeInt != float("infinity") else ""