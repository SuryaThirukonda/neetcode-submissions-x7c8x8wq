class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        std::unordered_map<int,int> m;
        
        for (int i: nums){
            if (m.contains(i)){
                return true;
            }
            m[i] = 1;

        }
        return false;
    }
};