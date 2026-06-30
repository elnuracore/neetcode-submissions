class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            dif = target - nums[i]
            if dif in nums and i != nums.index(dif):
                if i < nums.index(dif):
                    return [i, nums.index(dif)]
                else:
                    return [nums.index(dif), i]