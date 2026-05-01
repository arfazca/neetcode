public class Solution {
    public int[] TwoSum(int[] nums, int target) {
        Dictionary<int, int> prev = new Dictionary<int, int>();
        for (int i=0; i<nums.Length; i++) {
            int diff = target - nums[i];
            if (prev.ContainsKey(diff)) {
                return new int[] {prev[diff],i};
            }
            prev[nums[i]]=i;
        }
        return null;
    }
}
