import math


def main(z):
    s1 = 0
    for i in range(len(z)):
        s1 = s1 + 85 * math.floor(92 * z[i] ** 2 + z[i // 3] + 1)
    return s1
