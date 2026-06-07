class Solution {
public:
    vector<int> twoSum(vector<int>& numbers, int target) {
        vector<int> ans;
        int cnt = 1;
        while(numbers.size() > 0) {
            int need = target - *numbers.begin();
            
            auto it = find(numbers.begin(), numbers.end(), need);
            if(it != numbers.end()) {
                ans.push_back(int(numbers.begin()-numbers.begin()) + cnt);
                ans.push_back(int(it-numbers.begin()) + cnt);
                break;
            }
            numbers.erase(numbers.begin());
            cnt++;
        }
        return ans;
    }
};
