class Solution:
    def myPow(self, x: float, n: int) -> float:
        t = x
        for i in range(1, abs(n)):
            t *= x
            print ("t: ", t, ", x: ", x, ", n:", abs(n))
        return t if n > 0 else 1 / t