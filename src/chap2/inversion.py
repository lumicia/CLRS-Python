# 思考题 2-4


def cross_inversion_count(a: list[int], p: int, q: int, r: int) -> int:
    left = a[p : q + 1]
    right = a[q + 1 : r + 1]
    i = 0
    j = 0
    k = p
    inversions = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            a[k] = left[i]
            i += 1
        else:
            a[k] = right[j]
            j += 1
            inversions += len(left) - i
        k += 1

    if j == len(right):
        a[k : r + 1] = left[i:]

    return inversions


def inversion_count(a: list[int], p: int, r: int) -> int:
    inversions = 0
    if a == [] or len(a) == 1:
        return 0
    if p < r:
        q = (p + r) // 2
        inversions += inversion_count(a, p, q)
        inversions += inversion_count(a, q + 1, r)
        inversions += cross_inversion_count(a, p, q, r)

    return inversions
