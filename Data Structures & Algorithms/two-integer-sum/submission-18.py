class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        b = dict()
        for i, num in enumerate(nums):
            need = target - num
            if need in b:
                return [b[need], i]
            b[num] = i
            