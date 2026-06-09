class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        while left <= right:
            cur = (left + right)//2
            if target == nums[cur]:
                return cur
            elif target < nums[cur]:
                right = cur-1
            else:
                left = cur+1
        return -1
