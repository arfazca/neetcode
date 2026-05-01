public class Solution
{
    public int LongestConsecutive(int[] nums)
    {
        int longest = 0;
        HashSet<int> nHash = new HashSet<int>(nums);
        foreach (int num in nums)
        {
            int curr = 0;
            if (nHash.Contains(num+1+curr)) { curr++; }
            longest = Math.Max(curr,longest);
            console.WriteLine(longest);
        }
        return longest;
    }
}