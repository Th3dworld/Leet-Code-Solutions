class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        hashMap = dict()
        
        for char in s:
            hashMap[char] =  hashMap.get(char, 0) + 1
        
        for char in t:
            hashMap[char] =  hashMap.get(char, 0) - 1
            if hashMap[char] < 0:
                return False
        
        return True