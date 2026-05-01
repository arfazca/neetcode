class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1=="0" or num2=="0": return "0"
        if num1 < num2: return self.multiply(num2, num1)

        res, zero = "", 0
        for i in range(len(num2)-1,-1,-1):
            cur = self.mul(num1, num2[i], zero)
            res = self.add(cur, res)
            zero += 1
        return res

    def mul(self, top: str, bottom: str, zero: int) -> str:
        i, carry = len(top) - 1, 0
        bottom = int(bottom)
        res = []

        while i >= 0 or carry:
            current = int(top[i]) if i >= 0 else 0
            prod = (current * bottom) + carry
            res.append(str(prod % 10))
            carry = prod // 10
            i -= 1
        return ''.join(res[::-1]) + zero * '0'
    
    def add(self, num1: str, num2: str) -> str:
        i, j, carry = len(num1) - 1, len(num2) - 1, 0
        res = []

        while i >= 0 or j >= 0 or carry:
            curr_1 = int(num1[i]) if i >= 0 else 0
            curr_2 = int(num2[j]) if j >= 0 else 0
            addition = curr_1 + curr_2 + carry
            res.append(str(addition % 10))
            carry = addition // 10
            i -= 1
            j -= 1
        return ''.join(res[::-1])