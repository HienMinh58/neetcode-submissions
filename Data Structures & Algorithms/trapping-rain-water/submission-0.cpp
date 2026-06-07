class Solution {
public:
    int trap(vector<int>& height) {
        int n=height.size();
        int left=1;
        int right=n-2;
        int lMax=height[left-1];
        int rMax=height[right+1];
        int res=0;
        while(left<=right){
            if(rMax<=lMax){
                res += max(0, rMax-height[right]);
                rMax = max(rMax, height[right]);
                right--;
            }
            else{
                res += max(0, lMax-height[left]);
                lMax = max(lMax, height[left]);
                left++;
            }
        }
        return res;
    }
};
