class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #Check if lengths are equal
        if len(s)  != len(t):
            return False
        
        #create dict to map letter to number of occurrences
        letter_to_occur = dict()
        for char in s:
            letter_to_occur[char] = letter_to_occur.get(char,0) + 1
        for char in t:
            letter_to_occur[char] = letter_to_occur.get(char,0) - 1
            if letter_to_occur[char] < 0: 
                return False
        return True