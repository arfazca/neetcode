class Solution:
    def lengthOfLongestSubstring(self, string: str) -> int:
        s = set()
        L, result = 0, 0

        for R in range(len(string)):
            while (string[R] in s):
                s.remove(string[L])
                L += 1
            s.add(string[R])
            result = max(result, R - L + 1)
        
        return result