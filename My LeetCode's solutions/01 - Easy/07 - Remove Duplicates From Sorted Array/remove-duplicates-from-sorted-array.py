from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        # NOTE: 
        nums[:] = sorted(set(nums))
        return len(nums)


        # NOTE:
        # i: int = 0
        # while i < len(nums) - 1:
        #     if nums[i] == nums[i + 1]:
        #         nums.pop(i)
        #         i = i
        #     else:
        #         i += 1

        # return len(nums)


solution = Solution()


nums = [-3, -1, 0, 0, 0, 3, 3]
answer = solution.removeDuplicates(nums=nums)
print(f"return: {answer} {nums}")


nums = [-1, 0, 0, 0, 0, 3, 3]
answer = solution.removeDuplicates(nums=nums)
print(f"return: {answer} {nums}")


nums = [1, 1, 2, 3]
answer = solution.removeDuplicates(nums=nums)
print(f"return: {answer} {nums}")


nums = [1, 2, 3]
answer = solution.removeDuplicates(nums=nums)
print(f"return: {answer} {nums}")


nums = [1, 2]
answer = solution.removeDuplicates(nums=nums)
print(f"return: {answer} {nums}")


nums = [1, 1]
answer = solution.removeDuplicates(nums=nums)
print(f"return: {answer} {nums}")


nums = [1, 1, 2]
answer = solution.removeDuplicates(nums=nums)
print(f"return: {answer} {nums}")


nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
answer = solution.removeDuplicates(nums=nums)
print(f"return: {answer} {nums}")
