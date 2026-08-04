class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        n = len(grid)
        row_counts = Counter(tuple(row) for row in grid)
        
        result = 0
        for j in range(n):
            col = tuple(grid[i][j] for i in range(n))
            result += row_counts[col]
        
        return result