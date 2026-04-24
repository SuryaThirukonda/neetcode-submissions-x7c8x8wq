class Solution {
public:
    vector<int> findOrder(int numCourses, vector<vector<int>>& prerequisites) {
        vector<vector<int>> adj(numCourses);
        vector<int> ind(numCourses, 0);

        //build adjacency list
        //build indegree list
        for (auto i : prerequisites){
            (adj[i[1]]).push_back(i[0]);
            //b is before a
            ind[i[0]]++;
        }

        queue<int> q;
        for (int i= 0; i<ind.size(); i++){
            if (ind[i]==0){
                q.push(i);
            }
        }
        
        vector<int> output;
        while (!q.empty()){
            int top = q.front();
            q.pop();
            output.push_back(top);

            for (auto i : adj[top]){
                ind[i]--;
                if (ind[i]==0){
                    q.push(i);
                }

            }
        }
        vector<int> empty = {};
        if (output.size() != ind.size()){
            return empty;
        }
        return output;


    }
};
