def number(s):
    number = ''
    for i in s:
        if i == '@':
            s = s.replace(number, '')
            s = s.replace('@', '', 1)
            number = number.replace('{', '')
            number = number.replace('}', '')
            number = number.split('.')

            return list(map(int, number)), s
        else:
            number += str(i)


def key(s):
    key = ''
    for i in s:
        if i == ';':
            s = s.replace(key, '')
            s = s.replace(';', '', 1)
            key = key.replace('"', '')
            return key, s
        else:
            key += str(i)


def main(s):
    s = s.replace('<data>', '')
    s = s.replace('</data>', '')
    s = s.replace('==>', '')
    s = s.replace('#', '')
    s = s.replace(' ', '')
    lst_value, s = number(s)
    lst_key, s = key(s)
    d = {lst_key: lst_value}
    counter = s.count('@')
    for i in range(counter):
        lst_value, s = number(s)
        lst_key, s = key(s)
        d.update({lst_key: lst_value})
    return d
