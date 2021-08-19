from typing import Union

# Python 用 `float("inf")` 表示无穷大。`inf` 也可写成 `Inf`、`INF`。
# 在 Python 3.10 中可以无需导入 Union，可以更方便地使用 `a: list[int | float]` 来表达。
def merge_with_sentinels(a: list[Union[int, float]], p: int, q: int, r: int) -> None:
    left = a[p : q + 1]
    right = a[q + 1 : r + 1]
    left.append(float("inf"))
    right.append(float("inf")) 
    i = 0
    j = 0

    for k in range(p, r + 1):
        if left[i] <= right[j]:
            a[k] = left[i]
            i += 1
        else:
            a[k] = right[j]
            j += 1


def merge_sort_with_sentinels(a: list[Union[int, float]], p: int, r: int) -> None:
    if p < r:
        q = (p + r) // 2
        merge_sort_with_sentinels(a, p, q)
        merge_sort_with_sentinels(a, q + 1, r)
        merge_with_sentinels(a, p, q, r)

if __name__=='__main__':
    a:list[Union[int,float]]=[2,3,1,6]
    merge_sort_with_sentinels(a,0,3)