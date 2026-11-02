import sys
from math import prod

with open(sys.argv[1]) as f:
    seq = "".join(f"{int(c, 16):04b}" for c in f.read())
    
def parse_packet(bits: str, pos: int = 0) -> tuple[int, int, int]:
    version = int(bits[pos:pos+3], 2)
    tid = int(bits[pos+3:pos+6], 2)
    pos += 6
    val = 0

    if tid == 4:
        literal_bits = ''
        while True:
            flag = bits[pos]
            literal_bits += bits[pos+1:pos+5]
            pos += 5
            if flag == '0':
                break
        val = int(literal_bits, 2)
    else:
        sub_values = []
        length = bits[pos]
        pos += 1
        if length == '0':
            total = int(bits[pos:pos+15], 2)
            pos += 15
            end = pos + total
            while pos < end:
                sub, sub_value, pos = parse_packet(bits, pos)
                version += sub
                sub_values.append(sub_value)
        else:
            num_packets = int(bits[pos:pos+11], 2)
            pos += 11
            for _ in range(num_packets):
                sub, sub_value, pos = parse_packet(bits, pos)
                version += sub
                sub_values.append(sub_value)

        if      tid == 0: val = sum(sub_values)
        elif    tid == 1: val = prod(sub_values)
        elif    tid == 2: val = min(sub_values)
        elif    tid == 3: val = max(sub_values)
        elif    tid == 5: val = int(sub_values[0] > sub_values[1])
        elif    tid == 6: val = int(sub_values[0] < sub_values[1])
        elif    tid == 7: val = int(sub_values[0] == sub_values[1])

    return version, val, pos

part1, part2, _ = parse_packet(seq, 0)
print(f"Part 1: {part1}")
print(f"Part 2: {part2}")