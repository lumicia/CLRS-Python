def sum_of_two_binary_intergers(a: list[int], b: list[int]) -> list[int]:
    c = [0] * (len(a) + 1)
    carry = 0

    for i in range(len(a) - 1, -1, -1):
        # remainder
        c[i + 1] = (a[i] + b[i] + carry) % 2
        # quotient
        carry = (a[i] + b[i] + carry) // 2

    c[0] = carry
    return c
