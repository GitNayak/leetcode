class Solution:
    def countCommas(self, n: int) -> int:
        ans = 0
        start = 1000
        commas = 1

        while start <= n:
            end = start * 1000 - 1

            right = min(n, end)

            count = right - start + 1

            ans += count * commas

            start *= 1000
            commas += 1

        return ans