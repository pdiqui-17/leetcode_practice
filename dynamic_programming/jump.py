#This is the 45th leetcode problem
#The Question ask for the minimum jump from the initial point (indexed 0) to the last one
#Where a jump is defined by the ability to move from a current index to next one unless thier
# distance is greater than the value of the current one
#This one is my initial Accepted idea which gradually pick the farthest point which can move to the
# current point in just only one jump, this is easily found but it takes O(n^2) time complexity  
def jump(nums) :
    last_point = len(nums) -1
    count = 0
    while last_point > 0 :
        for i in range (0,last_point):
            if i+nums[i] >= last_point:
                count+=1
                last_point = i
                break
    return count

