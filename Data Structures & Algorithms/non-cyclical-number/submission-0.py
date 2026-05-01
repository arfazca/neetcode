class Solution:
    def isHappy(self, n: int) -> bool:
        D = set()
        
        while n not in D:
            D.add(n)
            n = self.SQRT(n)
            if n==1: return True
        return False
    
    def SQRT(self, n: int) -> int:
        out = 0

        while n:
            d = n % 10
            d = d ** 2
            out += d
            n = n // 10
        return out