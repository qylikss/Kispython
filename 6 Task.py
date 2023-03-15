def main(x):
    if x[2] == 2000:
        return 12
    elif x[2] == 2014:
        x0 = {1967: 6, 2002: 7, 2005: 8}
        x3 = {1967: 9, 1969: 10, 1998: 11}
        x1 = {'EBNF': 5, 'LIMBO': 'x0', 'AGDA': 'x3'}
        if x1.get(x[1]) == 5:
            return x1.get(x[1])
        else:
            if x1.get(x[1]) == 'x3':
                return x3.get(x[3])
            else:
                return x0.get(x[0])
    elif x[2] == 1993:
        x3 = {1967: 0, 1969: 1, 1998: 2}
        x1 = {'EBNF': 'x3', 'LIMBO': 3, 'AGDA': 4}
        if x1.get(x[1]) == 3 or x1.get(x[1]) == 4:
            return x1.get(x[1])
        else:
            return x3.get(x[3])