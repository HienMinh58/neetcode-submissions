class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(t) != len(s):
            return False
        s_s = {}
        t_s = {}
        for ch in s:
            if ch not in s_s:
                s_s[ch] = 1
            s_s[ch] += 1
        for ch in t:
            if ch not in t_s:
                t_s[ch] = 1
            t_s[ch] += 1
        if t_s == s_s and len(t) == len(s) :
            return True
        return False