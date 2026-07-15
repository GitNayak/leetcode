class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        window_sum = 0

        for i in range(k):
            window_sum += nums[i]

        maximum_sum = window_sum

        for i in range(k, len(nums)):
            window_sum += nums[i]      
            window_sum -= nums[i - k]  

            if window_sum > maximum_sum:
                maximum_sum = window_sum

        return maximum_sum / k