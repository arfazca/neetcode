public class Solution {
    public List<List<int>> ThreeSum(int[] nums) {
        Array.Sort(nums);
        List<List<int>> result = new List<List<int>>();
        for (int i=0; i<nums.Length; i++)
        {
            int L = i+1, R = nums.Length - 1;
            if (i==0 && nums[i]>0) break;
            if (i>0 && nums[i]==nums[i-1]) continue;
            while (L < R)
            {
                int sumTotal = nums[i] + nums[L] + nums[R];
                if (sumTotal>0)         { R--; }
                else if (sumTotal <0)   { L++; }
                else if (sumTotal==0)   
                { 
                    result.Add(new List<int> {nums[i], nums[L], nums[R]}); 
                    L++; R--;
                    while (L<R && nums[L]==nums[L-1]) { L++; }
                }
            }
        }
        return result;
    }
}