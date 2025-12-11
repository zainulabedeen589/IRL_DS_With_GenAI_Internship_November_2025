from typing import List


class Solution:
    def numTeams(self, rating: List[int]) -> int:
        n = len(rating)
        teams = 0

        for j in range(n):
            left_smaller = left_larger = 0
            right_smaller = right_larger = 0

            # count left side
            for i in range(j):
                if rating[i] < rating[j]:
                    left_smaller += 1
                else:
                    left_larger += 1

            # count right side
            for k in range(j + 1, n):
                if rating[k] > rating[j]:
                    right_larger += 1
                else:
                    right_smaller += 1

            # increasing + decreasing teams
            teams += left_smaller * right_larger
            teams += left_larger * right_smaller

        return teams
