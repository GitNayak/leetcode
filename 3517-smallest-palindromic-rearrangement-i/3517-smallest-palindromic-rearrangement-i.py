from collections import Counter 
class Solution:
    def smallestPalindrome(self, s: str) -> str:
        cnt = Counter(s)

        first = []
        middle = ""

        for ch in sorted(cnt):
            first.append(ch * (cnt[ch] // 2))
            if cnt[ch] % 2:
                middle = ch

        first = "".join(first)
        return first + middle + first[::-1]