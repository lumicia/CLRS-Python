# 练习 2.1-3

from typing import Optional


def linear_search(a: list[int], v: int) -> Optional[int]:
    for i in range(len(a)):
        if a[i] == v:
            return i

    return None
