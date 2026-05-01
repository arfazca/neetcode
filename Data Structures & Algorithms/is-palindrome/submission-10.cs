public class Solution {
    public bool IsPalindrome(string s) {
        int L = 0, R = s.Length-1;
        while (L < R)
        {
            while (L<R && !AlphaNum(s[L])) { L++; }
            while (L<R && !AlphaNum(s[R])) { R--; }
            if (char.ToLower(s[L])!=char.ToLower(s[R])) { return false; } 
            L++; R--; 
        }
        return true;
    }

    public bool AlphaNum(char c)
    {
        return (c >= 'A' && c <= 'Z') || (c >= 'a' && c<= 'z') || (c>='0' && c<='9');
    }
}
