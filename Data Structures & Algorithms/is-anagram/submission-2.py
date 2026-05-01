class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        cart=[char for char in s]
        print(cart)
        for i, char in enumerate(t):
            if char in cart:
                cart.remove(char)
            else:
                return False
        return True
            
