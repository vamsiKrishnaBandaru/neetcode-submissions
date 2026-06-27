class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l, r = 0, len(matrix) - 1
        while l <= r:
            mid = (l + r) // 2
            if matrix[mid][0] <= target and matrix[mid][-1] >= target:
                a, b = 0, len(matrix[0]) - 1
                arr = matrix[mid]
                while a <= b:
                    m = (a + b) // 2
                    if arr[m] == target:
                        return True
                    elif arr[m] < target:
                        a = m + 1
                    else:
                        b = m - 1
                return False
            elif (matrix[mid][0]) < target:
                l = mid + 1
            else:
                r = mid - 1
        return False
