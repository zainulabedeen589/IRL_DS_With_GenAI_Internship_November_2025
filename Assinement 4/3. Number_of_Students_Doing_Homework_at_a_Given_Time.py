from typing import List


class Solution:
    def busyStudent(
        self, startTime: List[int], endTime: List[int], queryTime: int
    ) -> int:
        # The number of students is the length of either startTime or endTime array
        num_students = len(startTime)
        busy_students_count = 0

        # Iterate through all students using their index 'i'.
        for i in range(num_students):
            start = startTime[i]
            end = endTime[i]

            # Check the condition: is queryTime within the inclusive interval [start, end]?
            # The student is busy if their start time is less than or equal to queryTime
            # AND their end time is greater than or equal to queryTime.
            if start <= queryTime and queryTime <= end:
                busy_students_count += 1

        return busy_students_count
