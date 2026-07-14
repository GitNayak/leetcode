class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        freq = defaultdict(int)
        res = 0

        for i in nums:
            need = k - i

            if freq[need] > 0:
                res += 1
                freq[need] -= 1
            else:
                freq[i] += 1

        return res
