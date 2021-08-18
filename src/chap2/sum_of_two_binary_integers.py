# 练习 2.1-4
# 注意高低位在数组中下标应该是倒着的，以及数组 c 的对应元素下标。

def sum_of_two_binary_intergers(a: list[int], b: list[int]) -> list[int]:
    c = [0] * (len(a) + 1)
    carry = 0
    for i in range(len(a) - 1, -1, -1):
        # 余数
        c[i + 1] = (a[i] + b[i] + carry) % 2
        # 商
        carry = (a[i] + b[i] + carry) // 2
    c[0] = carry
    return c
