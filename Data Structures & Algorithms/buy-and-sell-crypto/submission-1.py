class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_sum = 0
        for i in range(len(prices)-1):
            for j in range(i+1, len(prices)):
                if max_sum < prices[j] - prices[i]:
                    max_sum = prices[j] - prices[i]

        if max_sum > 0:
            return max_sum
        else:
            return 0
