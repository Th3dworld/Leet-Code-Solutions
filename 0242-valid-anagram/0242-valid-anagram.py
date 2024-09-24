class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(t) != len(s):
            return False
        
        occur_s = {}
        occur_t = {}
        
        for i in range(len(s)):
            occur_s[s[i]] = occur_s.get(s[i],0) + 1
            occur_t[t[i]] = occur_t.get(t[i],0) + 1
            
        return (occur_s == occur_t)
        