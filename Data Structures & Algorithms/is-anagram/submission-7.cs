public class Solution {
    public bool IsAnagram(string s, string t) {
        if (s.Length != t.Length) { return false; }
        Dictionary<char, int> S = new Dictionary<char, int>();
        Dictionary<char, int> T = new Dictionary<char, int>();
        for (int i=0; i<s.Length; i++) 
        {
            S[s[i]] = S.GetValueOrDefault(s[i], 0) + 1;
            T[t[i]] = T.GetValueOrDefault(t[i], 0) + 1;
        }
        return S.OrderBy(k=>k.Key).SequenceEqual(T.OrderBy(k=>k.Key));
    }
}
