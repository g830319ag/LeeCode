#### 1351. Count Negative Numbers in a Sorted Matrix Easy ####
class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        
        n, m = len(grid), len(grid[0])
        def binary_search(data):
            left = 0
            right = len(data) - 1
            while left <= right:
                mid = int((left + right) / 2)
                if data[mid] >= 0:    
                    left = mid + 1
                else:  
                    right = mid - 1
                
            return left
        
        count = 0
        for vector in grid:
            count += binary_search(vector)
        
        return n*m - count
        