class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        countS, countT = Counter(t), Counter(s)
        return countS == countT