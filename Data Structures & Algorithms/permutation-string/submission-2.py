class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2): return False
        s1map = {}
        window = {}
        
        # Build pattern map
        for c in s1:
            s1map[c] = s1map.get(c, 0) + 1
            
        # Build first window
        for i in range(len(s1)):
            window[s2[i]] = window.get(s2[i], 0) + 1
        
        if s1map == window: return True
        
        # Slide window
        for i in range(len(s1), len(s2)):
            # Add new char
            window[s2[i]] = window.get(s2[i], 0) + 1
            # Remove old char
            window[s2[i-len(s1)]] -= 1
            if window[s2[i-len(s1)]] == 0:
                del window[s2[i-len(s1)]]
            
            if s1map == window: return True
        
        return False