class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #check if strings are of equal length
        if len(s) != len(t):
            return False
        #create dictionary to map letter to occurence
        hashMap1 = dict()
        hashMap2 = dict()
        for (char1,char2) in zip(s,t):
            hashMap1[char1] = hashMap1.get(char1,0) + 1
            hashMap2[char2] = hashMap2.get(char2,0) + 1
        return hashMap1 == hashMap2
            
        
        