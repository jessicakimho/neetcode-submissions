class Solution {
public:
    bool isAnagram(string s, string t) {
        // two hashmaps
        // count character frequencies, maps should be equal

        if (s.size() != t.size()){
            return false;
        }

        std::unordered_map<char, int> s_freq;
        std::unordered_map<char, int> t_freq;

        for (char c : s){
            s_freq[c]++;
        }
        for (char c : t){
            t_freq[c]++;
        }

        return s_freq == t_freq;
    }
};
