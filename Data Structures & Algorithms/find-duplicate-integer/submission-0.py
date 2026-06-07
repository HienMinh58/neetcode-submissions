class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        hmap = {None: None}
        n = len(nums)
        i = 0
        
        while n:
            if nums[i] not in hmap:
                hmap[nums[i]] = 1
            else:
                return nums[i]
            n -= 1
            i += 1
        
