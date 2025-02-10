"""Real interview question."""


def sum_contiguous(list_of_nums: list, target: int) -> bool:
    """Check if there are contiguous blocks that sum up to target."""
    if target in list_of_nums:
        return True

    if sum(list_of_nums) < target:
        return False

    for i in range(len(list_of_nums)):
        current_sum = 0

        for j in range(i, len(list_of_nums)):
            current_sum += list_of_nums[j]

            if current_sum == target:
                return True

    return False
