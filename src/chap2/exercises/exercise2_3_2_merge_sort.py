def merge(a: list[int], p: int, q: int, r: int) -> None:
    left = a[p : q + 1]
    right = a[q + 1 : r + 1]
    i = 0
    j = 0
    k = p

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            a[k] = left[i]
            i += 1
        else:
            a[k] = right[j]
            j += 1
        k += 1

    # because len(left) >= len(right)
    if j == len(right):
        a[k : r + 1] = left[i:]


def merge_sort(a: list[int], p: int, r: int) -> None:
    if p < r:
        q = (p + r) // 2
        merge_sort(a, p, q)
        merge_sort(a, q + 1, r)
        merge(a, p, q, r)
