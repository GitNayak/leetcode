class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        res = []

        def backtrack(curr, op_pra, clo_pra):
            if len(curr) == 2 * n:
                res.append(curr)
                return

            if op_pra < n:
                backtrack(curr + "(", op_pra + 1, clo_pra)

            if clo_pra < op_pra:
                backtrack(curr + ")", op_pra, clo_pra + 1)

        backtrack("", 0, 0)

        return res