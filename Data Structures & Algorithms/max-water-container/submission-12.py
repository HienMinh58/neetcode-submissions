class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights) 
        left = 0
        right = n - 1
        maxA=0
        while(left<right):
            Area = (right-left) * min(heights[left], heights[right])
            maxA = max(maxA, Area)
            if heights[left]<heights[right]:
                left+=1
            else:
                right-=1
        return maxA