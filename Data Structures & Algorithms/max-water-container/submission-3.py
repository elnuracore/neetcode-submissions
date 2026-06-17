class Solution:
    def maxArea(self, heights: List[int]) -> int:
        right = len(heights) - 1
        left = 0
        max_amount = 0
        
        while left < right:
            if heights[right] < heights[left]:
                amount = (right - left) * heights[right]
            else:
                amount = (right - left) * heights[left]
                
            if max_amount < amount:
                max_amount = amount
                
            if heights[right] < heights[left]:
                right -= 1
            else:
                left += 1
                
        return max_amount