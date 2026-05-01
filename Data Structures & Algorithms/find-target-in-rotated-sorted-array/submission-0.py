class Solution:
    def search(self, nums: List[int], target: int) -> int:
        L, R = 0, len(nums) - 1

        while L <= R:
            M = L + ((R - L) // 2)
            if (nums[M]==target):
                return M
            elif (nums[L]<=nums[M]):
                if (nums[L]<=target<nums[M]):
                    R = M - 1
                else:
                    L = M + 1
            elif (nums[M]<=nums[R]):
                if (nums[M]<target<=nums[R]):
                    L = M + 1
                else:
                    R = M - 1
        return -1
