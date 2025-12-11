from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # Initialize the two largest numbers found so far.
        # Since all constraints state nums[i] >= 1, we can initialize with 0
        # or negative infinity, but 0 is simple here.
        largest = 0
        second_largest = 0

        for num in nums:
            if num >= largest:
                # 'num' is the new largest. The old largest becomes the second largest.
                second_largest = largest
                largest = num
            elif num > second_largest:
                # 'num' is not the largest, but it is the new second largest.
                second_largest = num

        # Calculate the final result.
        return (largest - 1) * (second_largest - 1)
