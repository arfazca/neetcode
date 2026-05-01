class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t: return ""
        window, count = {}, {}
        for e in t: count[e]=1+count.get(e,0)
        have, need = 0, len(count)
        res, resL = [-1,-1], float("infinity")

        L = 0
        for R in range(len(s)):
            a=s[R]
            window[a]=1+window.get(a,0)
            if a in count and count[a]==window[a]: have+=1
            while have==need:
                if (R-L+1 < resL):
                    res=[L, R]
                    resL=R-L+1
                b=s[L]
                window[b]-=1
                if b in count and window[b]<count[b]: have-=1
                L+=1
        L,R=res
        return s[L:R+1] if resL!=float("infinity") else ""