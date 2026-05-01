class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        L, R = 1, max(piles)
        RES = R
        while (L<=R):
            hours, i = 0, 0
            K = L + ((R-L)//2)
            while i < len(piles):
                hours += math.ceil(float(piles[i])/K)
                i += 1
            if hours<=h:
                RES = K
                R = K - 1
            else: L = K + 1
        return RES