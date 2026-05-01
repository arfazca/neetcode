public class Solution {
    public int[] TwoSum(int[] numbers, int target) {
        int L = 0, R = numbers.Length - 1;
        while (L < R)
        {
            int sumTotal = numbers[L] + numbers[R];
            if (sumTotal>target) { R--; }
            else if (sumTotal<target) { L++; }
            else if (sumTotal==target) 
            { 
                return new int[] {L+1, R+1};
            }
        }
        return new int[0];
    }
}
