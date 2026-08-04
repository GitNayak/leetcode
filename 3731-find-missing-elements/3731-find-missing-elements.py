class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        lo , hi = min(nums), max(nums)

        present = set(nums)

        return [i for i in range(lo ,hi+1) if i not in present]