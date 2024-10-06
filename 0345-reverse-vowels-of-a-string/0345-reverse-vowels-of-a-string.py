class Solution:
    def reverseVowels(self, s: str) -> str:
        word = list(s)
        vowel = ['a','e','i','o','u']
        l,r = 0, len(word)-1
        while l<r:
            while l<r and word[l].lower() not in vowel:
                l += 1
            while l<r and word[r].lower() not in vowel:
                r -= 1
            if l<r:
                word[l],word[r] = word[r],word[l]
                l += 1
                r -= 1
        return "".join(word)