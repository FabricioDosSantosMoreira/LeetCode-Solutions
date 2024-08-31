from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        merged_array: List[int] = nums1 + nums2
        merged_array.sort()

        if len(merged_array) % 2 == 0:
            return ((merged_array[len(merged_array) // 2 - 1]) + (merged_array[len(merged_array) // 2])) / 2
        else:
            return merged_array[len(merged_array) // 2]
        

solution = Solution()


nums1: List[int] = [1, 3]
nums2: List[int] = [2]
answer = solution.findMedianSortedArrays(nums1=nums1, nums2=nums2)
print(f"return: {answer}")


nums1: List[int] = [1, 2]
nums2: List[int] = [3, 4]
answer = solution.findMedianSortedArrays(nums1=nums1, nums2=nums2)
print(f"return: {answer}")
