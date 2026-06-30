class Solution:
    def isPalindrome(self, s: str) -> bool:
        i = 0
        ss = "".join(char for char in s if char.isalnum())
        if len(s) == 0:
            return True
        while i < len(ss)//2:
            if ss[i].lower() != ss[len(ss)-i-1].lower():
                return False
            i += 1
        return True