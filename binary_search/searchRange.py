def searchRange(nums,target) :
    def findFirst(target,first,last):
            if last - first == 1:
                if nums[last] == target :
                    return last
                else : return -1
            mid = (last + first)//2
            if nums[mid] < target :
                return findFirst(target,mid,last)
            else : return findFirst(target,first,mid)
    def findLast(target,first,last):
        if last - first ==1:
              if nums[first]==target:
                   return first
              else: return -1
        mid = (last+first)//2
        if nums[mid] > target:
             return findLast(target,first,mid)
        else : return findLast(target,mid,last)
    if len(nums) == 0: return [-1,-1]
    if len(nums) == 1 and nums[0] == target : return [0]
    
    first = findFirst(target,0,len(nums))
    last = findLast(target,0,len(nums))
    if first == -1 and last == -1 : return [-1,-1]
    if first == -1 : return last
    if last == -1 : return first
    return [first,last]

