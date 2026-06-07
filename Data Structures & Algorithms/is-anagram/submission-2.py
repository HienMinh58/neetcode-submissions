class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        a = dict()
        for char in s:
            if char in a.keys():
                a[char] += 1
            else:
                a[char] = 1
        b = dict()
        for char in t:
            if char in b.keys():
                b[char] += 1
            else:
                b[char] = 1
        
        return a == b
        
