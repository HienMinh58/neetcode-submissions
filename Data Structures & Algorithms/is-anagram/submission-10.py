class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(t) != len(s):
            return False
        s_count = {}
        t_count = {}
        for ch in s:
            s_count[ch] = s_count.get(ch, 0) + 1
        for ch in t:
            t_count[ch] = t_count.get(ch, 0) + 1
        if t_count == s_count:
            return True
        return False