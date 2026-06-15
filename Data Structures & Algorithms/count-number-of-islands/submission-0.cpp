class Solution {
public:
    int n,m;
    int drow[4] = {-1,1,0,0};
    int dcol[4] = {0,0,1,-1};
    vector<vector<bool>> visited;
    void dfs(vector<vector<char>>& grid, int row, int col){
        visited[row][col] = true;
        for(int k=0;k<4;k++){
            int nrow = row + drow[k];
            int ncol = col + dcol[k];
            if(nrow >= 0 && nrow < n && ncol >= 0 && ncol < m){
                if(grid[nrow][ncol]=='1' && !visited[nrow][ncol]){
                    dfs(grid, nrow, ncol);
                }
            }
        }
    }
    int numIslands(vector<vector<char>>& grid) {
        n = grid.size();
        m = grid[0].size();
        visited.assign(n, vector<bool>(m, false));
        int count = 0;
        for(int i=0;i<n;i++){
            for(int j=0;j<m;j++){
                
                if(grid[i][j] == '1' && !visited[i][j]){
                    count++;
                    dfs(grid, i, j);
                }
            }
        }
        return count;
    }
};
