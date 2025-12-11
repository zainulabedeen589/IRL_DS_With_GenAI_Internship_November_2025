from typing import List


class Solution:
    def countBits(self, n: int) -> List[int]:
        # Initialize the DP array of size n + 1 with zeros.
        # dp[i] will store the number of 1's in the binary representation of i.
        dp = [0] * (n + 1)

        # The base case is dp[0] = 0. We start the loop from 1.
        for i in range(1, n + 1):
            # The calculation: dp[i] = dp[i // 2] + (i % 2)
            # 1. i // 2 is i right-shifted by 1 (removes the last bit).
            # 2. i % 2 is the value of the last bit (0 or 1).

            # Using bitwise operators for speed and clarity:
            # i >> 1 is equivalent to i // 2
            # i & 1 is equivalent to i % 2
            dp[i] = dp[i >> 1] + (i & 1)

        return dp
