class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        my_map = {}
        for i in range(len(nums)):
            find = target - nums[i]
            my_map[nums[i]] = i
            if find in my_map and nums.index(find) != i:
                return [nums.index(find), i]
            