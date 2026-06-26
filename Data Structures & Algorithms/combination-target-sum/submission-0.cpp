class Solution {
public:
    vector<int> nums;
    vector<int> path;
    vector<vector<int>> res;
    int sum = 0;
    void backtrack(int target, vector<int> nums,vector<vector<int>>& res,int sum, int start){
        if(sum == target){
            res.push_back(path);
            return;
        }
        if(sum > target){
            return;
        }
        for(int i=start;i<nums.size();i++){
            path.push_back(nums[i]);
            backtrack(target, nums, res, sum + nums[i], i);
            path.pop_back();
        }
    }
    vector<vector<int>> combinationSum(vector<int>& nums, int target) {
        vector<vector<int>> res;
        int sum = 0;
        backtrack(target, nums, res, sum, 0);
        return res;
    }
};
