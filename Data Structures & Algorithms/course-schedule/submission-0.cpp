class Solution {
public:
    bool canFinish(int numCourses, vector<vector<int>>& prerequisites) {
        vector<int> id(numCourses,0);
        vector<int> order;
        vector<vector<int>> adj(numCourses);

        

        for (int i = 0; i<prerequisites.size(); i++){
            id[prerequisites[i][0]]++;
            //increase indegree of [a] by 1
            adj[prerequisites[i][1]].push_back(prerequisites[i][0]);
            //build adj list too
        }
        int n = id.size();

        queue<int> q;
        for (int i =0; i<id.size(); i++){
            if (id[i]==0){
                q.push(i);
            }/*  */
        }

        int count = 0;
        while (!q.empty()){
            int top = q.front();
            q.pop();
            order.push_back(top);
            count ++;
            for (int i : adj[top]){
                id[i]--;
                if (id[i]==0){
                    q.push(i);
                }
            }


        }

        if (count != n){
            return false;
        }
        return true;
    }
};
