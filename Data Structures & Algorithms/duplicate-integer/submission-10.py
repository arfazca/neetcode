class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        s = {}
        for i in range(len(nums)):
            if nums[i] in s:
                s[nums[i]] += 1
                return True
            else:
                s[nums[i]] = 1
        return False