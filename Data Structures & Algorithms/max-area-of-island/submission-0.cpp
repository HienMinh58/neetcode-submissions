class Solution {
public:
    int n,m;
    vector<vector<bool>> visited;
    int drow[4] = {-1, 1, 0, 0};
    int dcol[4] = {0, 0, -1, 1};
    int dfs(const vector<vector<int>>& grid, int row, int col){
        if(row < 0 || row >= n || col < 0 || col >= m){
            return 0;
        }

        if(grid[row][col] != 1 || visited[row][col]){
            return 0;
        }

        visited[row][col] = true;
        int area = 1;
        for(int k=0;k<4;k++){
            int nrow = row + drow[k];
            int ncol = col + dcol[k];
            area += dfs(grid, nrow, ncol);
        }
        return area;
    }

    int maxAreaOfIsland(vector<vector<int>>& grid) {
        n = grid.size();
        m = grid[0].size();
        visited.assign(n, vector<bool>(m, false));
        int ans = 0;
        for(int i=0;i<n;i++){
            for(int j=0;j<m;j++){
                if(grid[i][j] == 1 && !visited[i][j]){
                    int area = dfs(grid, i, j);
                    ans = max(ans, area);
                }
            }
        }
        return ans;
    }
};
