class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        L, R = 1, max(piles)
        result = R
        while (L<=R):
            K=L+((R-L)//2)
            H,i=0,0
            while (i<len(piles)):
                H+=math.ceil(float(piles[i])/K)
                i+=1
            if (H<=h):
                result = K
                R=K-1
            else: L=K+1
        return result