class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        my_set = {}
        for i in range(len(nums)):
            find = target - nums[i]
            if find in my_set:
                return [nums.index(find), i]
            my_set[nums[i]] = i
            