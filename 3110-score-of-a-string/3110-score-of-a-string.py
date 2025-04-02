class Solution:
    def scoreOfString(self, s: str) -> int:
        l,r = 0,1
        score = 0

        while r < len(s):
            score += abs(ord(s[l]) - ord(s[r]))
            l += 1
            r += 1
        
        return score