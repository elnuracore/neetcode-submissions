class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums)-1
        min_num = 0
        if len(nums) == 1:
            return nums[0]
        while left < right:
            mid = (left+right) // 2
            if nums[mid] > nums[right]:
                left = mid + 1
                min_num = nums[right]
            else:
                right = mid
                min_num = nums[left]

        return min_num
