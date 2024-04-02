class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:

      ## Brute force O(n^2)
        # negative_count = 0
        # for row in grid:
        #     for column in row:
        #         if column < 0:
        #             negative_count +=1
        # return negative_count    

      ## Binary Search O(n log n)
        negative_count = 0
        for row in grid:
            low, high = 0, len(row) - 1 
            while low <= high:
                mid = (low + high) >> 1
                if row[mid] < 0:
                    high = mid - 1
                else:
                    low = mid + 1

            negative_count += len(row) - low  
        return negative_count        
        
