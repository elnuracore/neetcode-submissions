class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        right = 0
        my_set = set()
        max_len = 0
        while right < len(s):
            if not s[right] in my_set:
                my_set.add(s[right])
                max_len = max(max_len, right-left+1) 
                right += 1
            else:
                my_set.discard(s[left])
                left += 1
        return max_len