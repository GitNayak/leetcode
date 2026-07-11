class Solution:
    def compress(self, chars: List[str]) -> int:
        i = 0
        j = 0

        while i < len(chars):
            k = i

            while k < len(chars) and chars[i] == chars[k]:
                k += 1

            chars[j] = chars[i]
            j += 1

            if k - i > 1:
                for c in str(k - i):
                    chars[j] = c
                    j += 1

            i = k

        return j