class Solution:
    def numberOfEmployeesWhoMetTarget(
        self,
        hours: list[int],
        target: int,
    ) -> int:
        result = 0

        for hour in hours:
            if hour >= target:
                result += 1

        return result
        # return sum([1 for i, hour in enumerate(hours, start=1) if hour >= target])
