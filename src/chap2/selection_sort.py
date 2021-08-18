# 练习 2.2-2


def selection_sort(a: list[int]) -> None:
    for i in range(len(a) - 1):
        min_idx = i
        for j in range(i + 1, len(a)):
            if a[j] < a[min_idx]:
                min_idx = j

        a[min_idx], a[i] = a[i], a[min_idx]
