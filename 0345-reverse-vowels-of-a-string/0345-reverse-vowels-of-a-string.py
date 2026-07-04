class Solution:
    def reverseVowels(self, s: str) -> str:
        vowel = 'aeiouAEIOU'

        character = list(s)
        left = 0
        right = len(s)-1

        while left < right:
            if character[left] not in vowel:
                left += 1
            
            elif character[right] not in vowel:
                right -= 1
            
            else:
                character[left], character[right] = character[right],character[left]
                left += 1
                right -= 1
        return "".join(character)