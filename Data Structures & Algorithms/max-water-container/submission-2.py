class Solution:
    def maxArea(self, heights: List[int]) -> int:
        right = len(heights)-1
        left = 0
        if len(heights) == 2 and (heights[right]==0 or heights[left]==0):
            return 0
        max_amount = 1
        for i in range(len(heights)):
            if heights[right] < heights[left]:
                amount = (right-left) * heights[right]
            else:
                amount = (right-left) * heights[left]
            if max_amount < amount:
                max_amount = amount
            if heights[right] < heights[left]:
                right -= 1
            else:
                left += 1
        return max_amount