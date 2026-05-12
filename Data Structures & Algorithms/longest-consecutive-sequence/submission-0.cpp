class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        std::unordered_set<int> bub;
        for (int i : nums){
            bub.insert(i);
        }

        
        int max1 = 0;
        
        for (int x: bub){
            int curr = x;
            if(bub.count(curr-1)){
                continue;
            }
            int local = 1;
            while(bub.count(curr+1))
            {
                local++;
                curr++;
                
            }
            max1 = std::max(local,max1);
            
        }

        return max1;

    }
};
