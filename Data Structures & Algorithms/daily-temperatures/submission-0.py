class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        stack = []
        for cur in range(len(temperatures)):
            while stack and temperatures[cur] > temperatures[stack[-1]]:
                poped_day = stack.pop()
                result[poped_day] = cur - poped_day
                pass
            stack.append(cur)
        return result