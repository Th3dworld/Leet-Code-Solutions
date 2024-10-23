class Solution:
    def firstUniqChar(self, s: str) -> int:
        Map = Counter(s)
        for i,c in enumerate(s):
            if Map[c] == 1:
                return i
        return -1