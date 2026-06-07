class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        last_pos = {}
        max_len = 0
        start = 0
        
        if len(s) == 0 or len(s) == 1:
            return len(s)

        for i, char in enumerate(s):
            if char in last_pos and last_pos[char] >= start:
                start = last_pos[char] + 1
            last_pos[char] = i
            max_len = max(max_len, i - start + 1)
        return max_len