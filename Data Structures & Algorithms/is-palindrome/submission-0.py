class Solution:
    def isPalindrome(self, s: str) -> bool:
        clearStr = ""
        for char in s:
            if char.isalnum():
                clearStr += char.lower()

        return clearStr == clearStr[::-1]

        
