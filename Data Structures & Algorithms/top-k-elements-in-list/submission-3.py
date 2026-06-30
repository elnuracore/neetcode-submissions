class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        my_map = {}
        for i in range(len(nums)):
            my_map[nums[i]] = 1 + my_map.get(nums[i], 0)
        sorted_map = sorted(my_map.items(), key = lambda x : x[1], reverse=True)
        sorted_key = [pair[0] for pair in sorted_map]
        return sorted_key[:k]

         