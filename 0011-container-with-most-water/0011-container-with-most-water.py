class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxArea = 0
        lp = 0
        rp = len(height)-1
        while lp < rp:
            width = rp - lp
            h = min(height[lp],height[rp])
            currArea = width * h
            maxArea = max(currArea,maxArea)

            if height[lp] < height[rp]:
                lp += 1
            else:
                rp -= 1
        return maxArea