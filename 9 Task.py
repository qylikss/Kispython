def main(table):
    n = len(table)
    first = list()
    second = list()
    third = list()
    fourth = list()
    for i in range(n):
        if table[i][0] == '1':
            first.append('true')
        else:
            first.append('false')
    for i in range(n):
        second.append(table[i][1].replace('.', '-'))
    for j in range(n):
        third.append(table[j][2].partition('@')[0])
    for j in range(n):
        fourth.append(table[j][3] + '000')
    new_table = [first, second, third, fourth]
    new_table = [list(i) for i in zip(*new_table)]
    return new_table
