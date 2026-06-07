class Solution:
    def trap(self, heights: List[int]) -> int:
        n = len(heights)
        left = 1
        right = n - 2
        lmax = heights[left-1]
        rmax = heights[right+1]
        res = 0
        while(left<=right):
            if rmax<=lmax:
                res += max(0,rmax - heights[right])
                rmax = max(rmax, heights[right])
                right -= 1
            else:
                res += max(0, lmax-heights[left])
                lmax = max(lmax, heights[left])
                left += 1
        return res