class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
      if len(grid) == 0 or grid is None:
        return 0
      ans = 0
      
      # naturally, dfs() will be a recursive function
      def dfs(grid, i, j):
        # base case
        # we'll stop once either of i, j is less than zero or bigger than the bound, or grid[i][j] == 0
        if (i < 0 or j< 0 or i >= len(grid) or j >= len(grid[i]) or grid[i][j]== '0'):
          return
        # we'll sink once a cordinate has been visited and keep track of our continuous island
        grid[i][j] = '0'
        
        # now we have to make sure that we go all four directtions in search of the continuous island
        dfs(grid, i-1, j) # left
        dfs(grid, i+1, j) # right
        dfs(grid, i, j-1) # up
        dfs(grid, i, j+1) # down
        
        return 1
        
      for i in range(len(grid)):
        for j in range(len(grid[i])):
          if grid[i][j] == '1':
            ans += dfs(grid, i, j)
      return ans
