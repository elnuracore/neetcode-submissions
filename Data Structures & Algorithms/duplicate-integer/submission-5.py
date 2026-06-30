class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        A = set()
        for i in range(len(nums)):
            A.add(nums[i])
        if len(nums) != len(A):
            return True
        else:
            return False
        