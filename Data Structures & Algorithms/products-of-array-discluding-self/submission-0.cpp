class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        vector<int> postFix(nums.size());
        vector<int> preFix(nums.size());
        int index = 1;
        for(int i = 0; i < nums.size(); i++) {
            index *= nums[i];
            preFix[i] = index;
        }
        index = 1;
        for(int i = nums.size()-1; i > 0; i--){
            index *=nums[i];
            postFix[i] = index;
        }

        for(int i = 0; i < nums.size(); i++){
            if(i == 0) nums[i] = postFix[i+1];
            else if(i == nums.size()-1) nums[i] = preFix[i-1];
            else nums[i] = postFix[i+1] * preFix[i-1];
        }

        return nums;
    }
};
