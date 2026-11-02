class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])

        left = 0
        right = rows*cols - 1

        while left <= right:
            mid = (left + right) // 2

            row = mid // cols # what group its in
            col = mid % cols # where in that group 

            num = matrix[row][col]

            if num == target:
                return True
            elif num > target:
                right = mid - 1
            else:
                left = mid + 1
        return False