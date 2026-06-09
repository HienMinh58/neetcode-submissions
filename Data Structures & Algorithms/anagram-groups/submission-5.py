class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}

        for s in strs:
            count = [0] * 26
            for ch in s:
                count[ord(ch) - ord('a')] += 1
            key = tuple(count)
            groups.setdefault(key, []).append(s)
        return list(groups.values()) # group.values() is not a list, it is dict_value