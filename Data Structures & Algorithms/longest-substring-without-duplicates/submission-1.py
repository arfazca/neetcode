class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        S = {}
        for i in range(len(s)):
            if s[i] in S: 
                S.append(S.get(s[i])+1,0)
        print(S)
        return 0
