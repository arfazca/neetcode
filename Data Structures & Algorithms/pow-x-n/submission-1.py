class Solution:
    def myPow(self, x: float, n: int) -> float:
        t = 1
        for i in range(abs(n)):
            t *= x
            print ("t: ", t, ", x: ", x, ", n:", abs(n))
        return t if n > 0 else 1 / t