class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left = 0
        arr = []
        for i in matrix:
            arr.extend(i)
        right = len(arr)-1

        while left <= right:
            cur = (left+right) // 2
            if target == arr[cur]:
                return True
            elif arr[cur] < target:
                left = cur + 1
            else:
                right = cur - 1
        return False