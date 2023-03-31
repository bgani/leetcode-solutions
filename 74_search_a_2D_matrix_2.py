class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # Binary Search and virtual array approach O(log m*n)
        
        # rows count
        m = len(matrix)
        if (m == 0):
            return False
        
        # columns count
        n = len(matrix[0])

        left = 0 # left pointer
        right = m * n - 1 # right pointer = last element of matrix
        while left <= right:
            pivot_idx = (left + right) // 2
            # value of pivot element = pivot_idx // n - row index, pivot_idx % n - column index
            pivot_element = matrix[pivot_idx // n][pivot_idx % n]
            if target == pivot_element:
                return True
            else:
                if target < pivot_element:
                    right = pivot_idx - 1
                else: 
                    left = pivot_idx + 1
        return False