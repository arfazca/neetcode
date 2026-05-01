class Solution:
    def findMin(self, nums: List[int]) -> int:
        L, R, minimum = 0, len(nums) - 1, float("inf")
        while L <= R:
            M = L + ((R - L) // 2)
            minimum = min(minimum, nums[M])
            
            # If array is sorted from M to R
            if nums[M] <= nums[R]:
                # Update minimum potentially one last time with nums[L]
                # since we'll be breaking and won't check it otherwise
                minimum = min(minimum, nums[L])
                R = M - 1
                if L == R:  # Found the pivot point
                    break
            else:
                L = M + 1
        
        return minimum