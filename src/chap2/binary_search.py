# 练习 2.3-5

from typing import Optional


def binary_search(a: list[int], v: int, lo: int, hi: int) -> Optional[int]:
    if a==[]:
        return None
    while lo <= hi:
        mid = (lo + hi) // 2
        print(f'mid: {mid}')
        if a[mid] == v:
            return mid
        elif a[mid] < v:
            lo = mid + 1
            print(f'lo: {lo}')
        else:
            hi = mid - 1
            print(f'hi: {hi}')
    return None


def binary_search_recursive(a: list[int], v: int, lo: int, hi: int) -> Optional[int]:
    if a==[]:
        return None
    if lo > hi:
        return None
    mid = (lo + hi) // 2
    if a[mid] == v:
        return mid
    elif a[mid] < v:
        return binary_search_recursive(a, v, mid + 1, hi)
    else:
        return binary_search_recursive(a, v, lo, mid - 1)
