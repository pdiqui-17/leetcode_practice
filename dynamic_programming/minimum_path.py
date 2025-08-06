#This is the 120Th problem in leetcode, belongs to the dynamic programming topic
#I just show the answer not the question here.
#I have to find the minimum path from the top of triangle to its bottom 
#Create a path list which has the same shape with the triangle 
#The minimum value path to each point is calculated by chosing the smaller path element 
#plus with the value of the triangle list value
def minimumTotal(triangle):
    n = len(triangle)
    path = [[0]*n for _ in range(n)]
    for i in range(len(triangle[n-1])):
        path[n-1][i] = triangle[n-1][i]
    for i in range(n-2,-1,-1):
        for j in range(len(triangle[i])):
            path[i][j] = min(path[i+1][j],path[i+1][j+1])+triangle[i][j]
    return path[0][0]
triangle = [[-10]]
print(minimumTotal(triangle))
    