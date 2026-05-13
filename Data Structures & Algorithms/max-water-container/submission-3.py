class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1
        area = 0
        while l < r:
            h = min(heights[l], heights[r])
            new_area = h * (r-l)
            area = max(new_area, area)
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        
        return area
                