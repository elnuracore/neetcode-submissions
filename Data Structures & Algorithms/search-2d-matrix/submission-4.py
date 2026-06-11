class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left = 0
        rows = len(matrix)
        columns = len(matrix[0])
        right = rows * columns - 1
        while left <= right:
            cur = (left+right)//2
            r = cur // columns
            c = cur % columns
            cur = (left+right)//2
            if matrix[r][c] < target:
                left = cur + 1
            elif matrix[r][c] > target:
                right = cur - 1
            elif matrix[r][c] == target:
                return True
        return False


