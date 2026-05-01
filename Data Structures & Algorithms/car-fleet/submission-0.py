class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = [(p,q) for p,q in zip(position,speed)]
        pair.sort(reverse=True)
        stack=[]
        for p,q in pair:
            stack.append((target-p)/q)
            if len(stack)>=2 and stack[-2]>=stack[-1]: stack.pop()
        return len(stack)