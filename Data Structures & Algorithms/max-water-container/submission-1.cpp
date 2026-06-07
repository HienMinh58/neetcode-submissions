#include<bits/stdc++.h>
using namespace std;
class Solution {
public:
    int maxArea(vector<int>& heights) {
        int maxA=0;
        int n = heights.size();
        int left=0;
        int right=n-1;
        while(left<right) {
            if(heights[left]<heights[right]){
                int minH=min(heights[left], heights[right]);
                int newMax=minH*(right-left);
                maxA = max(maxA, newMax);
                left++;
            }
            else {
                int minH=min(heights[left], heights[right]);
                int newMax=minH*(right-left);
                maxA = max(maxA, newMax);
                right--;
            }
        }
        return maxA;
    }
};
