class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        checkList={}
        for i, num in enumerate(nums):
            complement = target-num
            if complement in checkList:
                return [checkList[complement], i]
            checkList[num]=i
        return []