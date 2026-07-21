class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        altitude = 0 
        height = 0

        for i in gain:
            altitude += i
            height = max(altitude,height)
        return height