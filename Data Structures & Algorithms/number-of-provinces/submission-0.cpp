class Solution {
public:

    void dfs(vector<vector<int>>&isConnected, vector<bool>& visited, int node){
            visited[node]=true;
            for (int i = 0; i< isConnected.size(); i++){
                if (isConnected[node][i] && !visited[i]){
                    dfs(isConnected, visited, i);
                }
            }
    }
    int findCircleNum(vector<vector<int>>& isConnected) {
        int n = isConnected.size();
        int provinces = 0; 

        vector<bool> visited(n,false);
        for (int i =0; i<n; i++){
            if (!visited[i]){
                dfs(isConnected, visited, i);
                provinces++;
            }
        }
        return provinces;
    }
};