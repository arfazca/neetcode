class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow1, fast = 0, 0
        
        print("LOOP1")
        while True:
            slow1 = nums[slow1]
            fast = nums[nums[fast]]
            print("SLOW1\t: [",slow1, "] FAST\t: [",fast,"]")
            if slow1 == fast: break
        
        slow2 = 0
        print("LOOP1")
        while True:
            slow1 = nums[slow1]
            slow2 = nums[slow2]
            print("SLOW1\t: [",slow1, "] SLOW2\t: [",slow2,"]")
            if slow1 == slow2: break
        return slow2