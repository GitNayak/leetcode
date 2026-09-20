class Solution:
    def reverseDegree(self, s: str) -> int:
        total = 0

        for pos, ch in enumerate(s, start=1):

            rev = 26 - (ord(ch) - ord('a'))

            total += rev* pos

        return total