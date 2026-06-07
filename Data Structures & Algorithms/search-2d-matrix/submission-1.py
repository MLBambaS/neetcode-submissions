class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def searchInRow(matrix: List[List[int]], target: int, row: int, start: int, end: int) -> bool:
            if matrix[row][start] > target or matrix[row][end] < target:
                return False
            middle = (start+end)//2
            if matrix[row][middle] == target: return True
            if matrix[row][middle] < target: return searchInRow(matrix, target, row, middle+1, end)
            else: return searchInRow(matrix, target, row, start, middle-1)

        def searchInMatrix(matrix: List[List[int]], target: int, start: int, end: int) -> bool:
            if matrix[start][0] > target or matrix[end][-1] < target:
                return False
            middle = (start+end)//2
            if matrix[middle][0] == target or matrix[middle][-1] == target: return True
            if matrix[middle][0] < target and matrix[middle][-1] > target: return searchInRow(matrix, target, middle, 0, len(matrix[middle])-1)
            if matrix[middle][-1] < target: return searchInMatrix(matrix, target, middle+1, end)
            else: return searchInMatrix(matrix, target, start, middle-1)
        return searchInMatrix(matrix, target, 0, len(matrix)-1)
        