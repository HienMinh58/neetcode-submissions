class Solution {
public:
    vector<int>path;
    
    void backtrack(vector<int> nums, int sum, vector<vector<int>> &res, int target, int start){
        if(sum == target){
            res.push_back(path);
            return;
        }
        if(sum > target){
            return;
        }
        for(int i = start; i < nums.size(); i++){
            path.push_back(nums[i]);
            backtrack(nums, sum + nums[i], res, target, i);
            path.pop_back();
        }
    }
    vector<vector<int>> combinationSum(vector<int>& nums, int target) {
        vector<vector<int>> res;
        int sum = 0;
        backtrack(nums, sum, res, target, 0);
        return res;
    }
};
