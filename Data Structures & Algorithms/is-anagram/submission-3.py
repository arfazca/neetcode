class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        cart=[char for char in s]
        for i, char in enumerate(t):
            if char in cart:
                cart.remove(char)
                print(cart)
            else:
                return False
        return True
            
