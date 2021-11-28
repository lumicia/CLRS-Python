def naive_polynomial_evaluation(a: list[int], x: int) -> int:
    if a == []:
        return 0
    y = 0

    for k in range(len(a)):
        m = 1
        for i in range(1, k + 1):
            m = m * x
        y += a[k] * m

    return y


def horner_rule(a: list[int], x: int) -> int:
    if a == []:
        return 0
    y = 0

    for k in range(len(a) - 1, -1, -1):
        y = a[k] + x * y

    return y
