# 思考题 2-2


def bubble_sort(a: list[int]) -> None:
    for i in range(len(a) - 1):
        for j in range(len(a) - 1, i, -1):
            if a[j] < a[j - 1]:
                a[j], a[j - 1] = a[j - 1], a[j]
