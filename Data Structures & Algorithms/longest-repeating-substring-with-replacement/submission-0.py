class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        right = 0
        max_len = 0
        max_count = 0  # Track max frequency of a single character
        counts = {}
        
        while right < len(s):
            ch = s[right]
            if ch in counts:
                counts[ch] += 1
            else:
                counts[ch] = 1
            # Update the max frequency seen in the window
            max_count = max(max_count, counts[ch])
            
            # Check validity using max_count
            if (right - left + 1) - max_count > k:
                counts[s[left]] -= 1
                left += 1   
            # Track the maximum length of a valid window
            max_len = max(max_len, right - left + 1)
            right += 1
        
        return max_len