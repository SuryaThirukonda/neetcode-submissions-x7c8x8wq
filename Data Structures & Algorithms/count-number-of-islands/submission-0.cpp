class Solution {
public:
    void dfs (int x, int y, vector<vector<char>>& grid){
        if (x >= 0 && x < grid.size() && y >= 0 && y < grid[x].size() && grid[x][y] == '1')
        {
            grid[x][y]='0';
            dfs(x-1, y,  grid);
            dfs(x,y-1,grid);
            dfs(x, y+1, grid);
            dfs(x+1, y, grid);

        }
        return;
        
        
        
    }
    int numIslands(vector<vector<char>>& grid) {
        int count = 0;
        for (int x = 0; x<grid.size(); x++){
            for (int y = 0; y<grid[0].size(); y++){
                if (grid[x][y]=='1'){
                    dfs(x,y, grid);
                    count++;
                }
            }
        }
        return count;
    }
};
