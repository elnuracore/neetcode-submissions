class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        right = 0
        max_count = 0
        max_len = 0
        counts = {}
        while right < len(s):
            ch = s[right]
            if ch in counts:
                counts[ch] += 1
            else:
                counts[ch] = 1
            max_count = max(max_count, counts[ch])
            if (right-left+1) - max_count > k:
                counts[s[left]] -= 1
                left += 1
            max_len = max(max_len, right-left+1)
            right += 1
        return max_len


