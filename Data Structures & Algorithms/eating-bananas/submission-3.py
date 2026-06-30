class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)
        hours_needed = 0
        while left < right:
            mid = (left + right) // 2
            hours_needed = 0
            for i in piles:
                hours_needed += math.ceil(i / mid)
            if hours_needed <= h:
                right = mid 
            else:
                left = mid + 1
        return left
