class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        count = {}

        for i in arr:
            if i in count:
                count[i] += 1
            else:
                count[i] = 1

        seen = set()

        for freq in count.values():
            if freq in seen:
                return False
            seen.add(freq)

        return True