import math


def main(n):
    if n == 0:
        return 0.52
    elif n == 1:
        return -0.51
    elif n >= 2:
        return 1 + 11 * main(n - 1) + (math.floor(main(n - 2))) ** 2