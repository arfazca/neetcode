class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        L, R = 1, max(piles)
        res=R
        while L<=R:
            M = L + ((R - L) // 2)
            hours = 0
            for p in piles:
                hours += float(p) // M
            if hours <= h:
                res = min(res,M)
                R = M - 1
            else:
                L = M + 1
        return res