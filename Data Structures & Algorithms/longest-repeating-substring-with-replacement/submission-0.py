class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        bag = {}
        L, maxf = 0, 0

        for R in range(len(s)):
            bag[s[R]] = 1 + bag.get(s[R], 0)
            maxf = max(maxf, bag[s[R]])

            if ((R - L + 1 - maxf) > k):
                bag[s[L]] -= 1
                L += 1
        return R - L + 1