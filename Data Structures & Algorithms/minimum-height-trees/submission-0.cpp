class Solution {
public:
    vector<int> findMinHeightTrees(int n, vector<vector<int>>& edges) {

        if (n==1) return {0};
        vector<vector<int>> adj(n);
        vector<int> ind(n,0);

        for (auto edge: edges){
            adj[edge[0]].push_back(edge[1]);
            adj[edge[1]].push_back(edge[0]);

            ind[edge[0]]++;
            ind[edge[1]]++;
        }


        queue<int> q; 
        for (int i =0; i<ind.size(); i++){
            if(ind[i]==1){
                q.push(i);
            }
        }
        int remaining = n;

        while(remaining>2){
            int size = q.size();
            remaining -=size;

            for (int i =0; i<size; i++){
                int vertex = q.front();
                q.pop();

                for (int neighbor: adj[vertex]){
                    ind[neighbor]--;
                    if (ind[neighbor]==1){
                        q.push(neighbor);
                    }
                }
            }
        }

        vector<int> result;
        while(!q.empty()){
            result.push_back(q.front());
            q.pop();
        }
        return result;
    }
};