from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        # NOTE: Time Complexity = O(n^2) 
        # 'n' is the length of the list 'nums'
        for i in range(len(nums)):
            for y in range(len(nums)):
                sum = nums[i] + nums[y]

                if (sum == target) and (i != y):
                    return [i, y]


        # NOTE: Time Complexity = O(n^2)
        # 'n' is the length of the list 'nums'
        # cont_a: int = 0
        # cont_b: int = 1

        # while cont_a <= len(nums):
        #     sum = nums[cont_a] + nums[cont_b]
        #     if (sum == target) and cont_a != cont_b:
        #         return [cont_a, cont_b]

        #     cont_b += 1
        #     if cont_b >= len(nums):
        #         cont_a += 1
        #         cont_b = 0
            

solution = Solution()

nums: List[int] = [2, 7, 11, 15]
target: int = 9
answer = solution.twoSum(nums=nums, target=target)
print(f"return: {answer}")


nums: List[int] = [2, 5, 5, 11]
target: int = 10
answer = solution.twoSum(nums=nums, target=target)
print(f"return: {answer}")


nums: List[int] = [3, 2, 4]
target: int = 6
answer = solution.twoSum(nums=nums, target=target)
print(f"return: {answer}")


nums: List[int] = [3, 3]
target: int = 6
answer = solution.twoSum(nums=nums, target=target)
print(f"return: {answer}")


nums: List[int] = [3, 2, 3]
target: int = 6
answer = solution.twoSum(nums=nums, target=target)
print(f"return: {answer}")
