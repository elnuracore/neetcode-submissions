class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left = 0
        right = len(matrix)-1
        arr = []
        for i in matrix:
            arr.extend(i)
        while left <= right:
            cur = (left+right) // 2
            if target in arr:
                return True
            elif arr[cur] < target:
                right = cur - 1
            else:
                left = cur + 1
        return False