# 练习 2.3-4
# 可以效仿归并排序，将递归的插入排序分为 `insert` 和 `insertion_sort_recursive` 两部分。


def insert(a: list[int], n: int) -> None:
    i = n - 1
    key = a[n]

    while i >= 0 and a[i] > key:
        a[i + 1] = a[i]
        i -= 1

    a[i + 1] = key


def insertion_sort_recursive(a: list[int], n: int) -> None:
    if n <= 0:
        return
    else:
        insertion_sort_recursive(a, n - 1)
        insert(a, n)
