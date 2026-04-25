class Solution {
public:

    int dfs(int x, int y, vector<vector<int>>& grid){
        if (x>-1 && y>-1 && x<grid.size() && y<grid[0].size()){
            //check bounds
            if( grid[x][y]){
                grid[x][y]=0;
                return 1 + 
                dfs(x+1,y,grid)+
                dfs(x-1,y,grid)+
                dfs(x,y+1,grid)+
                dfs(x,y-1,grid);
            }
            
            

        }
        return 0;

    }
    int maxAreaOfIsland(vector<vector<int>>& grid) {
        int max = 0;
        for (int i =0; i< grid.size(); i ++){
            for (int j = 0; j<grid[i].size(); j++){

                if (grid[i][j]==1){
                    int newMax = dfs(i,j,grid);
                    if (newMax>max){
                        max = newMax;
                    }
                }
                
            }
        }
        return max;
    }
};
