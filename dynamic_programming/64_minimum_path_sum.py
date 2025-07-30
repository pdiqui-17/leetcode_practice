# I ask for AI help in this question, the code below was done by the idea of create the min path
#to each square inside the grid, since to reach each square, we only have to way 
# its left square(if exist) and its above square(if exist) gradually caculate each min path correspond to each square 
# and we will have the min value path to the bottom left one 
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m,n=len(grid[0]), len(grid)
        min_path = [[0]*m for _ in range(n)]
        min_path[0][0]=grid[0][0]
        for i in range(1,n):
            min_path[i][0] = min_path[i-1][0]+grid[i][0]
        for i in range(1,m):
            min_path[0][i] = min_path[0][i-1]+grid[0][i]
        for i in range (1,n):
            for j in range(1,m):
                min_path[i][j] = min(min_path[i][j-1],min_path[i-1][j])+grid[i][j]
        return min_path[-1][-1]