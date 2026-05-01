class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        S, RNG = {}, 0
        L, R = 0, 0
        MAX = 0

        while R < len(s):
            S[s[R]] = 1 + S.get(s[R], 0)
            MAX=max(MAX, S[s[R]])

            while ((R-L+1)-MAX)>k:
                S[s[L]]-=1
                L+=1
            RNG = max(RNG, R-L+1)
            R+=1
        return RNG