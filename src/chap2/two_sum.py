# 练习 2.3-7

from typing import Optional


def two_sum(a: list[int], x: int) -> list[Optional[int]]:
    m = {}
    for j, k in enumerate(a):
        rem = x - a[j]
        if m.get(rem) is not None:
            i = m.get(rem)
            return [i, j]
        m[k] = j

    return [None, None]
