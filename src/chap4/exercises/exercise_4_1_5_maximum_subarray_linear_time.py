# Dynamic Programming using a list to store the maximum subarray
def find_maximum_subarray_dp(
    a: list[int], low: int, high: int
) -> tuple[int, int, int | float]:
    max_sum = float('-inf')
    dp = [float('-inf')] * (high - low + 1)
    dp[0] = a[0]

    if low == high:
        return low, high, a[low]

    for i in range(low + 1, high + 1):
        # dp[i] = max(dp[i - 1] + a[i], a[i])
        # max_sum = max(max_sum, dp[i])
        if dp[i - 1] + a[i] < a[i]:
            dp[i] = a[i]
            max_left = i
        else:
            dp[i] = dp[i - 1] + a[i]

        if dp[i] > max_sum:
            max_sum = dp[i]
            max_right = i

    return max_left, max_right, max_sum


def maximum_subarray_dp(a: list[int]) -> tuple[int, int, int | float]:
    return find_maximum_subarray_dp(a, 0, len(a) - 1)


# Dynamic Programming using a single variable to store the maximum subarray
def find_maximum_subarray_dp2(
    a: list[int], low: int, high: int
) -> tuple[int, int, int | float]:
    max_sum = float('-inf')
    dp = 0
    max_left = low
    max_right = low

    if low == high:
        return low, high, a[low]

    for i in range(low + 1, high + 1):
        # dp = max(dp + a[i], a[i])
        # max_sum = max(max_sum, dp)
        if dp + a[i] < a[i]:
            dp = a[i]
            max_left = i
        else:
            dp += a[i]

        if dp > max_sum:
            max_sum = dp
            max_right = i

    return max_left, max_right, max_sum


def maximum_subarray_dp2(a: list[int]) -> tuple[int, int, int | float]:
    return find_maximum_subarray_dp(a, 0, len(a) - 1)


# Kadane's algorithm
def find_maximum_subarray_kadane(
    a: list[int], low: int, high: int
) -> tuple[int, int, int | float]:
    max_sum = float('-inf')
    curr_sum = 0
    curr_low = low
    curr_high = low

    for j in range(low, high + 1):
        curr_high = j
        curr_sum += a[j]
        if curr_sum > max_sum:
            max_sum = curr_sum
            max_left = curr_low
            max_right = curr_high

        if curr_sum < 0:
            curr_sum = 0
            curr_low = j + 1

    return max_left, max_right, max_sum


def maximum_subarray_kadane(a: list[int]) -> tuple[int, int, int | float]:
    return find_maximum_subarray_kadane(a, 0, len(a) - 1)


# Greedy
def find_maximum_subarray_greedy(
    a: list[int], low: int, high: int
) -> tuple[int, int, int | float]:
    max_sum = float('-inf')
    sum = float('-inf')
    curr_low = low
    curr_high = low

    for j in range(low, high + 1):
        curr_high = j
        if sum > 0:
            sum += a[j]
        else:
            curr_low = j
            sum = a[j]
        if sum > max_sum:
            max_sum = sum
            max_left = curr_low
            max_right = curr_high

    return max_left, max_right, max_sum


def maximum_subarray_greedy(a: list[int]) -> tuple[int, int, int | float]:
    return find_maximum_subarray_greedy(a, 0, len(a) - 1)
