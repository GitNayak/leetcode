class Solution:
    def minimumPushes(self, word: str) -> int:
        pushes = 1
        ans = 0

        for i in range(len(word)):
            if i > 0 and i % 8 == 0:
                pushes += 1

            ans += pushes

        return ans