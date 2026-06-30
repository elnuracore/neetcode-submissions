class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            find = target - nums[i]
            if find in nums and i != nums.index(find):
                if i < nums.index(find):
                    return [i, nums.index(find)]
                else:
                    return [nums.index(find), i]