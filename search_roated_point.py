def break_point(nums, first, last):
    if last - first == 1:
        if nums[last] < nums[first]:
            return last
        else:
            return first  # Trả về vị trí đầu nếu mảng vẫn tăng
    mid = (first + last) // 2
    if nums[mid] > nums[last]:
        return break_point(nums, mid, last)
    else:
        return break_point(nums, first, mid)
nums =[8,9,10,11,12,1,2,3,4,5,7]
print(break_point(nums,0,len(nums)-1))   
