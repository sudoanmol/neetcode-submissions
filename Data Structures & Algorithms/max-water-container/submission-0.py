class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_area = 0
        l, r = 0, len(heights) - 1

        while l < r:
            h1 = heights[l]
            h2 = heights[r]
            area = 0

            if h1 > h2:
                area = h2 * (r-l)
                r-=1
            else:
                area = h1 * (r-l) # same for h1=h2, h2>h1
                l+=1

            if area > max_area:
                max_area = area

        return max_area