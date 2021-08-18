# 需要注意算法导论中的伪代码的下标从 1 开始，
# 用 Python 实现时需要做出相应改变。
def insertion_sort(a: list[int]) -> None:
    for j in range(1, len(a)):
        key = a[j]
        i = j - 1
        while i >= 0 and a[i] > key:
            a[i + 1] = a[i]
            i -= 1
        a[i + 1] = key
