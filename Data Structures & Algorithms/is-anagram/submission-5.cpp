class Solution {
public:
    bool isAnagram(string s, string t) {
        if (s.size() != t.size()) {
            return false;
        }

        unordered_map<char, int> S;
        unordered_map<char, int> T;
        for (int i = 0; i<s.size(); i++) {
            S[s[i]]++;
            T[t[i]]++;
        }
        return S==T;
    }
};
