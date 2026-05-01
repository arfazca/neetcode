class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2): return False
        S1, S2 = {}, {}
        
        # Build Pattern Map (S1)
        # Build First Window (S2)
        for i in range(len(s1)):
            S1[s1[i]] = S1.get(s1[i], 0) + 1 # MAP
            S2[s2[i]] = S2.get(s2[i], 0) + 1 # WINDOW
        if S1 == S2: return True
        
        # Slide Window
        L, R = 0, len(s1)
        while R < len(s2):
            # Add new char
            S2[s2[R]] = S2.get(s2[R], 0) + 1
            
            # Remove old char
            S2[s2[L]] -= 1
            if S2[s2[L]] == 0: del S2[s2[L]]
            if S1 == S2: return True
            L, R = L+1, R+1
        return False