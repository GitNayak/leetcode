class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:

        n = len(nums)

        # (value, original index)
        arr = [(nums[i], i) for i in range(n)]

        # Sort by value
        arr.sort()

        ans = [0] * n

        start = 0

        while start < n:
            end = start

            # Find the complete connected group
            while (
                end + 1 < n
                and arr[end + 1][0] - arr[end][0] <= limit
            ):
                end += 1

            # Get original indices of this group
            indices = []

            for i in range(start, end + 1):
                indices.append(arr[i][1])

            # Sort original indices
            indices.sort()

            # Values are already sorted
            for i in range(len(indices)):
                ans[indices[i]] = arr[start + i][0]

            start = end + 1

        return ans