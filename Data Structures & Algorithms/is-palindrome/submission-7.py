class Solution:
    def isPalindrome(self, s: str) -> bool:
        i = 0
        ss = "".join(char for char in s if char.isalnum())
        if len(s) == 0:
            return True
        return ss.lower() == ss[::-1].lower()