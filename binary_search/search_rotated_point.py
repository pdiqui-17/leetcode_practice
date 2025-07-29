class Solution:
    def search(self, nums: List[int], target: int) -> int:
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

        def binary_search_recursive(nums, target, left, right):
            if left > right:
                return -1  # không tìm thấy

            mid = (left + right) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                return binary_search_recursive(nums, target, mid + 1, right)
            else:
                return binary_search_recursive(nums, target, left, mid - 1)

        if not nums:
            return -1

        if len(nums) == 1:
            return 0 if nums[0] == target else -1

        index = break_point(nums, 0, len(nums) - 1)

        # Nếu không xoay
        if nums[index] <= target <= nums[-1]:
            return binary_search_recursive(nums, target, index, len(nums) - 1)
        else:
            return binary_search_recursive(nums, target, 0, index - 1)