def insert(a: list[int], n: int) -> None:
    i = n - 1
    key = a[n]

    while i >= 0 and a[i] > key:
        a[i + 1] = a[i]
        i -= 1

    a[i + 1] = key


def insertion_sort(a: list[int], n: int) -> None:
    if n <= 0:
        return
    else:
        insertion_sort(a, n - 1)
        insert(a, n)
