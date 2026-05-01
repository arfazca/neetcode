class Solution:
    def isPalindrome(self, s: str) -> bool:
        L, R = 0, len(s)-1 # 0-indexed
        while L < R: # L can't be the same as R
            while L<R and not self.alphanumeric(s[L]): L+=1
            while R>L and not self.alphanumeric(s[R]): R-=1
            target, reference = s[L].lower(), s[R].lower()
            if target!=reference: return False
            L, R = L+1, R-1
        return True
    def alphanumeric(self, c: str) -> bool:
        return (
            ord('A') <= ord(c) <= ord('Z') or
            ord('a') <= ord(c) <= ord('z') or
            ord('0') <= ord(c) <= ord('9')
        )