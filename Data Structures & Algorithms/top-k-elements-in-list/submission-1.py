class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        rr={}
        rk=[]
        for i in range(len(nums)):
            # if nums[i] in rr:
            rr[nums[i]]=1+rr.get(nums[i],0)
            # else:
                # rr[nums[i]]=1
        for key, val in rr.items():
            print(key,":",val)
            if (val >= k): rk.append(key)
        return rk