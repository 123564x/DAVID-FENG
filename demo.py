from typing import List


# 自己写的方法
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if target in nums:
            return nums.index(target)
        else:
            nums.append(target)
            nums.sort()
            return nums.index(target)


# 上课讲的方法
#     class Solution:
#         def searchInsert(self, nums: List[int], target: int) -> int:
#             left, right = 0, len(nums) - 1
#
#             while left <= right:
#                 middle = (left + right) // 2
#                 if nums[middle] < target:
#                     left = middle + 1
#                 else:
#                     right = middle - 1
#             return left

nums = [1, 3, 5, 6, 7]
target = 5
print(Solution().searchInsert(nums, target))
