class Solution {
public:
    
    vector<int> topKFrequent(vector<int>& nums, int k) {
        
        unordered_map<int,int> m;
        for (int i :nums){
            m[i]++;
        }

        priority_queue<pair<int,int>, vector<pair<int,int>>, std::greater<pair<int,int>>> pq;


        for (auto freq : m){
            pq.push({freq.second, freq.first});
            if (pq.size() >k){
                pq.pop();
            }
        }

        vector<int> ans;

        while(!pq.empty()){
            ans.push_back(pq.top().second);
            pq.pop();
        }

        return ans;
        
        
    }
};
