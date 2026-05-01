public class Solution {
    public int[] TwoSum(int[] nums, int target) {
        Dictionary<int, int> Map = new Dictionary<int, int>();
        for (int i=0; i<nums.Length; i++)
        {
            int diff = target-nums[i];
            if (Map.ContainsKey(diff))
            {
                return new int[] {Map[diff],i};
            }
            Map[nums[i]]=i;
        }
        return null; 
    }
}
