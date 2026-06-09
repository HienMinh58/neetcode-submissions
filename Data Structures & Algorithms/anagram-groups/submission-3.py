class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}

        for s in strs:
            count = [0] * 26 # 26 alphabets

            for char in s:
                count[ord(char) - ord('a')] += 1

            key = tuple(count) # tuple is immutable so it can be used as key, list is mutable

            groups.setdefault(key, []).append(s)
        return list(groups.values())