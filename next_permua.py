class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def single_loop(nums, index):
            for i in range(1,len(nums)-index):
                if nums[-i] > nums[index]:
                    nums[-i], nums[index] = nums[index], nums[-i]
                    return 0
            return 1
        for i in range(len(nums) - 2, -1, -1):
            if  single_loop(nums,i) == 0: 
                nums[i+1:] = reversed(nums[i+1:])
                break
        else:
                  nums[:] = sorted(nums)
