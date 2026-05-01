public class Solution
{
    public int LongestConsecutive(int[] nums)
    {
        int longest = 0;
        HashSet<int> nHash = new HashSet<int>(nums);
        foreach (int num in nums)
        {
            int curr = 1;
            while (nHash.Contains(num+curr)) 
            {
                Console.WriteLine(Convert.ToInt32(curr)); 
                curr++; 
            }
            longest = Math.Max(curr,longest);
        }
        return longest;
    }
}