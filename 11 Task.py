from struct import *

FMT = dict(
    char='c',
    int8='b',
    uint8='B',
    int16='h',
    uint16='H',
    int32='i',
    uint32='I',
    int64='q',
    uint64='Q',
    float='f',
    double='d'
)


def parse(buf, offs, ty, order='>'):
    pattern = FMT[ty]
    size = calcsize(pattern)
    value = unpack_from(order + pattern, buf, offs)[0]
    return value, offs + size


def parse_d(buf, offs):
    d1, offs = parse(buf, offs, 'uint32')
    d2, offs = parse(buf, offs, 'uint8')
    d3, offs = parse(buf, offs, 'int64')
    d4, offs = parse(buf, offs, 'int16')
    d5 = []
    for _ in range(3):
        val, offs = parse(buf, offs, 'int64')
        d5.append(val)
    return dict(D1=d1, D2=d2, D3=d3, D4=d4, D5=d5), offs


def parse_c(buf, offs):
    c1, offs = parse(buf, offs, 'int8')
    c2 = []
    for _ in range(4):
        val, offs = parse(buf, offs, 'int8')
        c2.append(val)
    c3, offs = parse(buf, offs, 'int32')
    c4, offs = parse(buf, offs, 'int32')
    return dict(C1=c1, C2=c2, C3=c3, C4=c4), offs


def parse_b(buf, offs):
    b1_size, offs = parse(buf, offs, 'uint32')
    b1_offset, offs = parse(buf, offs, 'uint16')
    b1 = []
    for _ in range(b1_size):
        val, b1_offset = parse(buf, b1_offset, 'char')
        b1.append(val)
    b1 = b''.join(b1).decode('utf-8')
    c_offset, offs = parse(buf, offs, 'uint16')
    b2, _ = parse_c(buf, c_offset)
    b3, offs = parse_d(buf, offs)
    b4, offs = parse(buf, offs, 'int8')
    return dict(B1=b1, B2=b2, B3=b3, B4=b4), offs


def parse_a(buf, offs):
    a1, offs = parse(buf, offs, 'uint32')
    a2, offs = parse(buf, offs, 'uint32')
    a3, offs = parse(buf, offs, 'int16')
    a4 = []
    for _ in range(2):
        b_offs, offs = parse(buf, offs, 'uint16')
        val, _ = parse_b(buf, b_offs)
        a4.append(val)
    return dict(A1=a1, A2=a2, A3=a3, A4=a4), offs


def main(stream):
    return parse_a(stream, 5)[0]
