class Solution:
    def findMin(self, nums: List[int]) -> int:
        L, R, minimum = 0, len(nums)-1, nums[0]

        while (L<=R):
            M = L + ((R - L) // 2)
            minimum = min(minimum, nums[M])
            if (nums[M]>=nums[R]): L = M + 1
            else: R = M - 1
        return min(minimum, nums[L])