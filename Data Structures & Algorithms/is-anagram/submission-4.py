class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        cart=[char for char in s]
        for i, char in enumerate(t):
            if char in cart:
                cart.remove(char)
            else:
                return False
        if len(cart) != 0:
            return False
        return True
            
