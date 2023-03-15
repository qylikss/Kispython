import math


def main(y):
    if y < -12:
        return ((24 * y - y * y) ** 6) / 33 - 1
    elif -12 <= y < 12:
        return 1 - 74 * (51 * y ** 3 + 66 * y) ** 3
    elif 12 <= y < 88:
        return 22 * y ** 2 - math.atan(y) ** 6 - 22 * y ** 5
    elif 88 <= y < 113:
        return y * y
    elif y >= 113:
        return 50 + 3 * math.log10(y) ** 5 + 54 * y ** 3