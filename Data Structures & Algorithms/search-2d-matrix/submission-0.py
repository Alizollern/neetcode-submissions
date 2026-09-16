class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False
        
        m = len(matrix)
        n = len(matrix[0])
        
        # Binary search pointers for the conceptual 1D array
        left = 0
        right = m * n - 1
        
        while left <= right:
            mid = left + (right - left) // 2
            
            # Convert 1D mid index into 2D coordinates
            mid_val = matrix[mid // n][mid % n]
            
            if mid_val == target:
                return True
            elif mid_val < target:
                left = mid + 1
            else:
                right = mid - 1
                
        return False