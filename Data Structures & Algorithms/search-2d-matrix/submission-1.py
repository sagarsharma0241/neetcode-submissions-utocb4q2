class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        top = 0
        bottom = len(matrix) - 1

        while top <= bottom:
            row = (bottom + top) // 2
            if target > matrix[row][-1] :
                top = row + 1
            elif target < matrix[row][0] :
                bottom = row - 1
            else:
                break
        if not (top <= bottom):
            return False

        l = 0
        r = len(matrix[row]) - 1
        while l <= r:
            
            m = (r + l)//2
            print (m)
            if matrix[row][m] > target:
                r = m - 1
            elif matrix[row][m] < target:
                l = m + 1
            else:
                return True
        return False
