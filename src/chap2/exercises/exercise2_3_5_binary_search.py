def binary_search(a: list[int], v: int, lo: int, hi: int) -> int | None:
    if a == []:
        return None

    while lo <= hi:
        mid = (lo + hi) // 2
        if a[mid] == v:
            return mid
        elif a[mid] < v:
            lo = mid + 1
        else:
            hi = mid - 1

    return None


def binary_search_recursively(a: list[int], v: int, lo: int, hi: int) -> int | None:
    if a == []:
        return None

    if lo > hi:
        return None

    mid = (lo + hi) // 2

    if a[mid] == v:
        return mid
    elif a[mid] < v:
        return binary_search_recursively(a, v, mid + 1, hi)
    else:
        return binary_search_recursively(a, v, lo, mid - 1)
