class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        s = {}
        for num in nums:
            if num not in s:
                s[num] = 1
            else:
                return True
        return False
