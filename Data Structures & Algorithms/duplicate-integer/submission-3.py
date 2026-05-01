class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        for i in range(len(nums)-1):
            if nums[i]==nums[i-1]:
                print(nums[i])
                return False
        return True