class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        
        std::vector<int> res;
        std::unordered_map<int, int> freq;

        for (int num : nums){
            freq[num]++;
        }

        std::vector<pair<int, int>> pairs;
        for (const auto& p : freq){
            pairs.push_back({p.second, p.first});
        }
        
        sort(pairs.rbegin(), pairs.rend());

        for (auto it = pairs.begin(); it != pairs.end() && res.size() < k; it++){
            res.push_back(it->second);
        }
        return res;
    }
};
