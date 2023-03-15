import math


def main(m, a):
    s1 = 0
    for i in range(1, m+1):
        s1 = s1 + 32 * math.exp(i) ** 2
    s2 = 0
    for c in range(1, a+1):
        s3 = 0
        for k in range(1, m+1):
            s3 = s3 + (88 + 89 * (1 + ((k**3) / 42) + (c / 44)) ** 7)
        s2 = s2 + s3
    return s1 + s2