class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        L, R = 0, 0
        D, out = deque(), []

        while R < len(nums):
            while D and nums[D[-1]] < nums[R]: D.pop()
            D.append(R)
            R += 1

            if L > D[0]: D.popleft()
            if (R+1 >= k):
                out.append(nums[D[0]])
                L += 1
            R += 1
        return out