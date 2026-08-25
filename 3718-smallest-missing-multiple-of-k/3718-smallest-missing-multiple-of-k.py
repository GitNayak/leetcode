class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        num = set(nums)

        mul = k

        while mul in num:
            mul += k

        return mul