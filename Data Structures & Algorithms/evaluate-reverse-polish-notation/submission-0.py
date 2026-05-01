class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        res=[]
        for s in tokens:
            if (s=="+"):
                a, b = res.pop(), res.pop()
                res.append(int(a) + int(b))
            elif (s=="-"):
                a, b = res.pop(), res.pop()
                res.append(int(b) - int(a))
            elif (s=="*"):
                a, b = res.pop(), res.pop()
                res.append(int(a) * int(b))
            elif (s=="/"):
                a, b = res.pop(), res.pop()
                res.append(int(float(b)) / int(a))
            else:
                res.append(int(s))
        return res[0]