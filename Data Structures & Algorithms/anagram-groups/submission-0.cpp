class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        //first loop through all strings
        unordered_map<string, vector<string>> m;
        vector<vector<string>> ans;
        //this map stores the root anagram as the key, and then stores vector as value
        for (string i : strs){
            string v = i;
            sort(v.begin(), v.end());
            m[v].push_back(i);
        }

        for (auto vec : m){
            ans.push_back(vec.second);
        }

        return ans;
    }
};
