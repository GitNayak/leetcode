class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        l = 0
        zero = 0
        res = 0

        for i in range(len(nums)):
            if nums[i] == 0:
                zero += 1

            while zero > 1:
                if nums[l] == 0:
                    zero -= 1
                l += 1
            res = max(res,i -l)
        return res