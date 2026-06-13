#include<bits/stdc++.h>
using namespace std;
class Solution {
public:
    string minWindow(string s, string t) {
        if(s.size()<t.size()){
            return "";
        }
        unordered_map<char, int> need_count;
        unordered_map<char, int> window_count;
        for(char ch : t){
            need_count[ch]++;
        }
        int need = need_count.size();
        int have = 0;
        int left = 0;
        int best_len = 1e8;
        int best_start = 0;
        int current_len;
        for(int right=0;right<s.size();right++){
            window_count[s[right]]++;
            if(need_count.count(s[right]) && need_count[s[right]] == window_count[s[right]]){
                have++;
            }
            while(have==need){
                char left_char = s[left];
                current_len = right - left + 1;
                if(current_len < best_len){
                    best_len = current_len;
                    best_start = left;
                }
                window_count[left_char]--;
                
                if(need_count.count(left_char) && need_count[left_char] > window_count[left_char]){
                    have--;
                }
                left++;
            }
        }
        return best_len == 1e8 ? "" : s.substr(best_start, best_len);
    }
};
