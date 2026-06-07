class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        unordered_set<int> s(nums.begin(), nums.end());
        int longest = 0;
        for(int num : nums) {
            if(s.find(num-1) == s.end()) {
                int currentLen = 1;
                int currentNum = num;
                while(s.find(currentNum+1) != s.end()) {
                    currentLen++;
                    currentNum++;
                }
                longest = max(longest, currentLen);
            }
            
        }
        return longest;
    }
};
