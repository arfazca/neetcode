class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2): return False
        S1, S2 = {}, {}
        
        # Build pattern map
        # Build first S2 Window
        for i in range(len(s1)):
            S1[s1[i]] = S1.get(s1[i], 0) + 1
            S2[s2[i]] = S2.get(s2[i], 0) + 1    
        
        if S1 == S2: return True
        
        # Slide Window
        for i in range(len(s1), len(s2)):
            # Add new char
            S2[s2[i]] = S2.get(s2[i], 0) + 1
            # Remove old char
            S2[s2[i-len(s1)]] -= 1
            if S2[s2[i-len(s1)]] == 0:
                del S2[s2[i-len(s1)]]
            
            if S1 == S2: return True
        
        return False