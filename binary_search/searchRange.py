#This is the 34th leetcode question named : Find First and Last Position of Element in Sorted Array
# To solve this, i try to find the first and the last occurrence of the target number in the array by the same algorithm
# Below is how the algorithm work, i choose find function to explain, find :
# Firstly, choose the midddle point of the array, if the middle point is smaller than the target that means 
# there is no target in left side of the current array, and we need to go on to the right one. 
# On the other hand, that tells us the start of the range maybe of the left side of this point, so we search on this side
# the function stop when the left element reach the first element of the array
def searchRange(nums, target):
    def findFirst(nums, target):
        left, right = 0, len(nums) - 1
        res = -1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] < target:
                left = mid + 1
            else:
                if nums[mid] == target:
                    res = mid
                right = mid - 1
        return res

    def findLast(nums, target):
        left, right = 0, len(nums) - 1
        res = -1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] > target:
                right = mid - 1
            else:
                if nums[mid] == target:
                    res = mid
                left = mid + 1
        return res

    first = findFirst(nums, target)
    last = findLast(nums, target)
    return [first, last]