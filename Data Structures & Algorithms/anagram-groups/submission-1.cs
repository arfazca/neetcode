public class Solution {
    public List<List<string>> GroupAnagrams(string[] strs) {
        var res = new Dictionary<string, List<string>>();
        foreach(var a in strs)
        {
            int[] count = new int[26];
            foreach (var b in a) { count[b-'a']++; }
            string countr = string.Join(",", count);
            if (!res.ContainsKey(countr)) { res[countr] = new List<string>(); }
            res[countr].Add(a); 
        }
        return res.Values.ToList<List<string>>();
    }
}