def find_maximum_subarray(
    a: list[int], low: int, high: int
) -> tuple[int, int, int | float]:
    max_sum = float('-inf')
    sum = 0
    max_left = max_right = 0

    if len(a) == 1:
        return low, high, a[0]

    for i in range(low, high + 1):
        sum = a[i]
        j = i
        while j < high:
            if max_sum <= sum:
                max_sum = sum
                max_left = i
                max_right = j
            sum += a[j + 1]
            j += 1

    return max_left, max_right, max_sum


def maximum_subarray(a: list[int]) -> tuple[int, int, int | float]:
    return find_maximum_subarray(a, 0, len(a) - 1)
