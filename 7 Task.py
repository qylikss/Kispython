def main(s):
    number = int(s)
    a1 = (number & 0b00000000000000001111111)
    a2 = (number >> 7) & 0b0000000000000011
    a3 = (number >> 9) & 0b00000000001111
    a4 = (number >> 13) & 0b1111111111
    lst = [('A1', str(a1)), ('A2', str(a2)), ('A3', str(a3)), ('A4', str(a4))]
    return lst
