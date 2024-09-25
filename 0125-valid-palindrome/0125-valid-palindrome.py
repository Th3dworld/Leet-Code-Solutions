class Solution:
    def isPalindrome(self, s: str) -> bool:
        res = ""
        
        for char in s:
            if char.isalpha() or char.isdigit():
                res += char.lower()
        return res == res[::-1]
        