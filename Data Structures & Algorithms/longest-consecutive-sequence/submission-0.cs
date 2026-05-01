public class Solution
{
    public int LongestConsecutive(int[] nums)
    {
        if (nums.Length == 0) return 0;
        HashSet<int> set = new HashSet<int>(nums);
        int longest = 0;
        foreach (int num in set)
        {
            if (!set.Contains(num - 1))
            {
                int current = num + 1;
                while (set.Contains(current)) { current++; }
                int length = current - num;
                if (length > longest) { longest = length; }
            }
        }
        return longest;
    }
}