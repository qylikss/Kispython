import math


def main(y, x):
    print(math.sqrt((70 * (13 - 90 * x - 92 * y * y) ** 2 - 1) /
                    (62 * math.acos(y) ** 5 - 79 * x ** 4)) + y ** 6
          - math.acos(y ** 3 + x ** 2 + x / 51) ** 7)