class Solution:
    def isPalindrome(self, s: str) -> bool:
        string = ""
        
        for ch in s:
            if ch.isalnum():
                string += ch.lower()
        
        l,r = 0, len(string) - 1
        
        while l <= r:
            if string[l] != string[r]:
                return False
            else:
                l += 1
                r -= 1
        
        return True