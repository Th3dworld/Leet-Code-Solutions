class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #return false if the strings are not the same size
        if len(s) != len(t):
            return False
        #create dictionary to store values
        letterFrequency = dict()
        #populate dictionary with letters in s as keys
        #and increment value by 1 
        for l in s:
            letterFrequency[l] = 1 + letterFrequency.get(l,0)
        #check if the the letters in t are in the populated dictionary
        #decrement by 1
        for l in t:
            letterFrequency[l] = letterFrequency.get(l, 0) - 1
            #If the letter frequency is less than 0 then return False
            if letterFrequency[l] < 0:
                return False
        #Everything has passed the tests
        return True