class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""
        from collections import Counter, defaultdict
        need_count = Counter(t)
        window_count = defaultdict(int)

        need = len(need_count)
        have = 0

        best_start = 0
        best_len = float("inf")

        left = 0
        for right, char in enumerate(s):
            window_count[char] += 1
            if char in need_count and need_count[char] == window_count[char]:
                have += 1
            while need == have:
                current_len = right - left + 1
                left_char = s[left]
                window_count[left_char] -= 1
                if left_char in need_count and need_count[left_char] > window_count[left_char]:
                    have -= 1
                if current_len < best_len:
                    best_len = current_len
                    best_start = left
                left += 1
        return "" if best_len == float("inf") else s[best_start:best_start + best_len]