class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        most_common = Counter(nums).most_common(k)
        numbers = [pair[0] for pair in most_common]
        return numbers
