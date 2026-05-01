class Solution:
    def isPalindrome(self, s: str) -> bool:
        if (len(s)%2)!=0:
            return False
        cart=[char for char in s[0:len(s)//2] if char != ' ']
        t = [char for char in s[0:len(s)//2:-1] if char!= ' ']
        for i, num in enumerate(t):
            if num != cart[i]:
                return False
        return True
        