public class Solution {
    public bool hasDuplicate(int[] nums) {
        return new Hashset<int>(nums).Count < nums.Length;
    }
}