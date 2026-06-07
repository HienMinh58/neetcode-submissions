class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""
        from collections import Counter, defaultdict

        need_count = Counter(t)
        window_count = defaultdict(int)

        best_len = float("inf")
        best_start = 0

        need = len(need_count)
        have = 0

        left = 0 
        for right, char in enumerate(s):
            window_count[char] += 1

            if char in need_count and need_count[char] == window_count[char]:
                have += 1
            
            while have == need:
                left_char = s[left]
                window_count[left_char] -= 1
                if left_char in need_count and need_count[left_char] > window_count[left_char]:
                    have -= 1
                current_len = right - left + 1
                if current_len < best_len:
                    best_len = current_len
                    best_start = left
                left += 1
        return "" if best_len == float("inf") else s[best_start:best_start + best_len]