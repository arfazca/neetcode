public class Solution {
    public int CalPoints(string[] operations) {
       Stack<int> S = new Stack<int>();
       int result = 0;
       foreach (var op in operations) {
            if (op=="+") {
                int top1 = S.Pop();
                int top2 = S.Peek();
                int sum = top1+top2;
                S.Push(top1);
                S.Push(sum); result+=sum;
            }
            else if (op=="D") {
                int T = S.Peek() * 2;
                S.Push(T); result += T; 
            } 
            else if (op=="C") {
                result -= S.Pop();
            }
            else {
                int T = int.Parse(op);
                S.Push(T); result+=T;
            }
       }
       return result;
    }
}