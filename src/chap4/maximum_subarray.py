def find_max_crossing_subarray(
    a: list[int], low: int, mid: int, high: int
) -> tuple[int, int, int | float]:
    left_sum = float('-inf')
    sum: int = 0

    for i in range(mid, low - 1, -1):
        sum = sum + a[i]
        if sum > left_sum:
            left_sum = sum
            max_left = i

    right_sum = float('-inf')
    # Rename sum to sum2 as mypy report an error
    sum2: int = 0

    for j in range(mid + 1, high + 1):
        sum2 = sum2 + a[j]
        if sum2 > right_sum:
            right_sum = sum2
            max_right = j

    return (max_left, max_right, left_sum + right_sum)


def find_maximum_subarray(
    a: list[int], low: int, high: int
) -> tuple[int, int, int | float]:
    if high == low:
        return (low, high, a[low])
    else:
        mid = (low + high) // 2
        left_low, left_high, left_sum = find_maximum_subarray(a, low, mid)
        right_low, right_high, right_sum = find_maximum_subarray(a, mid + 1, high)
        cross_low, cross_high, cross_sum = find_max_crossing_subarray(a, low, mid, high)
        if left_sum >= right_sum and left_sum >= cross_sum:
            return (left_low, left_high, left_sum)
        elif right_sum >= left_sum and right_sum >= cross_sum:
            return (right_low, right_high, right_sum)
        else:
            return (cross_low, cross_high, cross_sum)


def maximum_subarray(a: list[int]) -> tuple[int, int, int | float]:
    return find_maximum_subarray(a, 0, len(a) - 1)
