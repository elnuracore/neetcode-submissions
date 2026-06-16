class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        current_streak = 1
        longest_streak = 1
        if len(nums) == 0:
            return 0

        for i in range(len(nums)-1):
            if nums[i+1]-nums[i] == 1:
                current_streak += 1
                if current_streak > longest_streak:
                    longest_streak = current_streak
            elif nums[i+1] == nums[i]:
                continue
            else:
                current_streak = 1
            
        return longest_streak