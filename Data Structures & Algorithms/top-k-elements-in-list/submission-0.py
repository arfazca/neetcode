class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        rr={}
        rk=[]
        for i in range(len(nums)):
            if nums[i] in rr:
                rr[nums[i]]=1+rr.get(nums[i],0)
            else:
                rr[nums[i]]=1
        for k, v in rr.items():
            print(k,":",v)
            if (v > k): rk.append(k)
        return rk