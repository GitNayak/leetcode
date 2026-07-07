class Solution:
    def sumAndMultiply(self, n: int) -> int:
        S = ""
        summ = 0

        for i in str(n):
            if i != '0':
                S += i
                summ += int(i)

        if S == "":
            return 0
        return int(S) * summ