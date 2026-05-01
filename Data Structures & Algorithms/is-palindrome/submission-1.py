class Solution:
    def isPalindrome(self, s: str) -> bool:
        # if (len(s)%2)!=0:
        #     return False
        cart=[char.lower() for char in s[0:len(s)//2] if char != ' ']
        print(cart)
        t = [char.lower() for char in s[:len(s)//2-1:-1] if char!= ' ']
        print(t)
        for i, num in enumerate(t):
            if num != cart[i]:
                return False
        return True
        