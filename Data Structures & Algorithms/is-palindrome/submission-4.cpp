class Solution {
public:
    bool isPalindrome(string s) {
        
        string t = "";
        for(char c : s) {
            if(isalnum(c)) {
                t += tolower(c);
            }
        }
        if(t.length() == 1 || t.length() == 0) return true;
        int len = t.size();
        int left = 0;
        int right = len-1;
        bool ans = false;
        while(left < right) {
            if(t[left] == t[right]) {
                ans = true;
                left++;
                right--;
            }
            else {
                return false;
            }
        }
        return ans;
    }
};
